#Name : Daniel Haimov
#ID : 311351647


# 1 :
def create_tuple(n):
    if n == 1:
        return (1,)

    return create_tuple(n - 1) + (n,)


result = create_tuple(1000)
print(result)

# 2 :
def create_tuple(n): # מהסעיף הקודם
    if n == 1:
        return (1,)

    return create_tuple(n - 1) + (n,)


def sum_tuple(t):
    if len(t) == 0:
        return 0

    return t[0] + sum_tuple(t[1:])


numbers = create_tuple(1000)

result = sum_tuple(numbers)

print(result)

# 3 :

def lcm(a, b, current=None):
    if current is None:
        current = max(a, b)

    if current % a == 0 and current % b == 0:
        return current

    return lcm(a, b, current + 1)

#4 :

def is_palindrome_number(n):
    def check(s):
        if len(s) <= 1:
            return True

        if s[0] != s[-1]:
            return False

        return check(s[1:-1])

    return check(str(n))

#5 :

def is_palindrome_alphanumeric(text):
    final_letters = {
        'ך': 'כ',
        'ם': 'מ',
        'ן': 'נ',
        'ף': 'פ',
        'ץ': 'צ'
    }

    cleaned = ''.join(
        map(
            lambda ch: final_letters.get(ch, ch.lower()),
            filter(lambda ch: ch.isalnum(), text)
        )
    )

    return cleaned == cleaned[::-1]


def main():
    text = input("enter text: ")

    if text.strip() == "":
        print("invalid input")
    else:
        print(is_palindrome_alphanumeric(text))


main()

# 6 :

def recursive_sort(lst):
    if len(lst) <= 1:
        return lst

    smallest = min(lst)
    new_lst = lst.copy()
    new_lst.remove(smallest)

    return [smallest] + recursive_sort(new_lst)


def sort_all(lists):
    if len(lists) == 0:
        return []

    return [recursive_sort(lists[0])] + sort_all(lists[1:])


def sortedzip(lists):
    return zip(*sort_all(lists))

#7 :

def encode_rle(text):
    if text == "":
        return ""

    count = 1

    def count_same(i):
        if i >= len(text) or text[i] != text[0]:
            return i
        return count_same(i + 1)

    end = count_same(1)

    return text[0] + str(end) + encode_rle(text[end:])

def main():
    text = input("enter text: ")

    if text.strip() == "":
        print("invalid input")
    else:
        print(encode_rle(text))


main()


# **********Lazy Evaluation, Generators ************** :


# 1 :

#  without Lazy Evaluation :

# : א

import sys
import time

def create_numbers():
    return list(range(10001))


start = time.perf_counter()

numbers = create_numbers()

end = time.perf_counter()

print("Time:", end - start)
print("Memory:", sys.getsizeof(numbers))
print("Type:", type(numbers)) # נותן גם את הטיפוס

# : ב

start = time.perf_counter()

first_5000 = numbers[:5000]

end = time.perf_counter()

print("Time:", end - start)
print("Memory:", sys.getsizeof(first_5000))
print("Type:", type(first_5000))

#  without Lazy Evaluation : (א + ב)

import sys
import time


def create_numbers_lazy():
    return (x for x in range(10001))


def first_5000_lazy(numbers):
    return (x for i, x in enumerate(numbers) if i < 5000)


# סעיף א'
start = time.perf_counter()

numbers = create_numbers_lazy()

end = time.perf_counter()

print("Original type:", type(numbers))
print("Original memory:", sys.getsizeof(numbers))
print("Original time:", end - start)


# סעיף ב'
start = time.perf_counter()

first_5000 = first_5000_lazy(numbers)

end = time.perf_counter()

print("New type:", type(first_5000))
print("New memory:", sys.getsizeof(first_5000))
print("New time:", end - start)


# 2 :

def prime_generator():
    num = 2

    while True:
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num

        num += 1


# 3 :

def e_generator(x):
    n = 0
    total = 0
    factorial = 1

    while True:
        if n > 0:
            factorial *= n

        total += (x ** n) / factorial

        yield total

        n += 1