#Names : Daniel Haimov
#ID's : 311351647


# 1 :
linear_func = lambda x: x / 2 + 2

#: א
numbers = list(range(10001))
new_list = list(map(linear_func, numbers))

#: ב
from functools import reduce
total = reduce(lambda x, y: x + y, new_list)


#: ג
from functools import reduce
import time

numbers = list(range(10001))
linear_func = lambda x: x / 2 + 2
new_list = list(map(linear_func, numbers))

# סכימת זמנים באמצעות פונקציית- העל reduce
start = time.perf_counter()

total_reduce = reduce(lambda x, y: x + y, new_list)

end = time.perf_counter()
reduce_time = end - start


# סכימת זמנים איטרטיבית באמצעות for
start = time.perf_counter()

total_loop = 0
for num in new_list:
    total_loop += num

end = time.perf_counter()
loop_time = end - start


print("Reduce sum:", total_reduce)
print("Reduce time:", reduce_time)

print("Loop sum:", total_loop)
print("Loop time:", loop_time)

#: ד

from functools import reduce

numbers = list(range(10001))

linear_func = lambda x: x / 2 + 2

total = reduce( lambda total, x: total + linear_func(x), numbers, 0 )

print(total)

# 2 :
numbers = list(range(1, 10001))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

#: א

from functools import reduce

numbers = list(range(1, 10001))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

even_func = lambda x, sub_list: reduce(
    lambda a, b: a * b,
    sub_list[:sub_list.index(x) + 1]
)

odd_func = lambda x, next: x / 2 + 2 + next

#: ב

even_results = list(map(lambda x: even_func(x, even_numbers), even_numbers))

odd_result = reduce(odd_func, odd_numbers)

print(even_results)
print(odd_result)


#: ג

even_results = list(
    map(lambda x: even_func(x, even_numbers), even_numbers))

odd_results = list(map(lambda x: odd_func(x, x), odd_numbers))


even_sum = reduce(lambda x, y: x + y, even_results)
odd_sum = reduce(lambda x, y: x + y, odd_results)

print("Even sum:", even_sum)
print("Odd sum:", odd_sum)


# 3 :

#: א
def is_armstrong(n):
    k = len(str(n))

    return sum(map(lambda digit: int(digit) ** k, str(n))) == n

#: ב
def armstrong_range(n1, n2):
    return list( filter(is_armstrong, range(n1, n2 + 1)) )

#: ג
def main():
    user_input = input("Enter a positive integer: ")

    if not user_input.isdigit() or int(user_input) <= 0:
        print("invalid input")
        return

    n = int(user_input)

    print(armstrong_range(1, n))


main()

# 4 :

#: א

from datetime import date, timedelta
import calendar

def dates_with_jump(month, jump):
    days_in_month = calendar.monthrange(2026, month)[1]

    return list(map(
            lambda day: date(2026, month, day),
            range(1, days_in_month + 1, jump)
        ) )

# 5 :

#: א
def power_function(power):
    return lambda x: x ** power

#: ב
def powers_map(n):
    return map(power_function, range(n))

def main():
    n = int(input("Enter number of powers: "))

    result = powers_map(n)

    print(type(result))

    base = int(input("Enter base: "))

    answer = tuple(
        map(lambda func: func(base), result)
    )

    print(answer)


main()

#: ג
import math

def e_approx(x, power):
    return sum(
        map(
            lambda n: x ** n / math.factorial(n),
            range(power + 1) )
    )


# 6 :

def task_manager():
    tasks = {}

    def add_task(task, status="incomplete"):
        if task not in tasks:
            tasks[task] = status

    def get_tasks():
        return tasks.copy()

    def complete_task(task):
        if task in tasks:
            tasks[task] = "complete"

    return {
        "add_task": add_task,
        "get_tasks": get_tasks,
        "complete_task": complete_task
    }

tasks_manager = task_manager()

# Add tasks
tasks_manager["add_task"]("Write email")
tasks_manager["add_task"]("Shopping", "in progress")
tasks_manager["add_task"]("Homework")

# Get the list of tasks
current_tasks = tasks_manager["get_tasks"]()
print(current_tasks)

# Mark a task as complete
tasks_manager["complete_task"]("Write email")

# Get tasks again
current_tasks = tasks_manager["get_tasks"]()
print(current_tasks)

# 7 :

#: א
def clean_spaces(text):
    return text.strip()


def capitalize_text(text):
    return text.title()


def add_stars(text):
    return "***" + text + "***"

#: ב
def create_pipeline():
    return lambda x: x

def add_to_pipeline(pipeline_fn, new_fn):
    return lambda x: new_fn(pipeline_fn(x))

#: ג

def main():
    pipeline = create_pipeline()

    pipeline = add_to_pipeline(pipeline, clean_spaces)
    pipeline = add_to_pipeline(pipeline, capitalize_text)
    pipeline = add_to_pipeline(pipeline, add_stars)

    text = input("enter text: ")

    if text.strip() == "":
        print("invalid input")
    else:
        print(pipeline(text))


main()
