#Names : Daniel Haimov
#ID's : 311351647

# 1 :

# : א
def get_penta_num(n):
    return n * (3 * n - 1) // 2 # הסימן "//" מחזיר תמיד תוצאת חלוקה שלמה (בפייתון רק "/" מחזיר ערך נקודה 0 , כמו למשל 12.0)

# : ב

def pentaNumRange(n1, n2):
    return list(map(get_penta_num, range(n1, n2))) #  ה- map בעצם תפעיל את הפונקצייה "get_penta_num" עבור על ערך בטווח של ה- range לא כולל את n2

# 2 :

def sum_digit(num):
    if not isinstance(num, int):
        return "invalid input"

    return sum(map(int, str(abs(num))))

def main():
 try:
    num = int(input("enter number: "))
    print(sum_digit(num))
 except ValueError:
    print("invalid input")

 if __name__ == "__main__":
        main()


# 3 :

# : א
def normalize_text(text):
    text = text.lower()
    text = text.replace(" ", "")
    text = sorted(text)
    text = "".join(text)
    return text

# : ב

def are_anagrams(text1 , text2):
    return normalize_text(text1) == normalize_text(text2)

def main():
        text1 = input("enter first text: ")
        text2 = input("enter second text: ")

        if text1.replace(" ", "") == "" or text2.replace(" ", "") == "":
            print("invalid input")
        else:
            print(are_anagrams(text1, text2))

if __name__ == "__main__":
        main()

# 4 :

def calculate_gematria(word):
    gematria = {
        'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5,
        'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10,
        'כ': 20, 'ך': 20, 'ל': 30, 'מ': 40, 'ם': 40,
        'נ': 50, 'ן': 50, 'ס': 60, 'ע': 70,
        'פ': 80, 'ף': 80, 'צ': 90, 'ץ': 90,
        'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400
    }

    return sum(gematria.get(letter, 0) for letter in word)

# 5 :

# : א

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

# : ב
def twin_prime(num):
    if not is_prime(num):
        return False

    return is_prime(num - 2) or is_prime(num + 2)


def main():
    num = int(input("enter number: "))

    if num < 2 or not is_prime(num):
        print("invalid input")
    else:
        if is_prime(num - 2):
            print(num - 2)
        elif is_prime(num + 2):
            print(num + 2)

if __name__ == "__main__":
    main()


# : ג

def twin_prime_dict(n):
    result = {}

    for num in range(2, n + 1):
        if is_prime(num):
            twin = twin_prime(num)

            if twin is not None:
                result[num] = twin

    return result

# 6 :

def add_3_dicts(d1, d2, d3):
    result = {}

    for key in d1:
        result[key] = tuple(set(
            [d1[key]] +
            ([d2[key]] if key in d2 else []) +
            ([d3[key]] if key in d3 else [])
        ))

    for key in d2:
        if key not in result:
            result[key] = tuple(set(
                [d2[key]] +
                ([d3[key]] if key in d3 else [])
            ))

    for key in d3:
        if key not in result:
            result[key] = (d3[key],)

    return result

# 7 :

# : א

def multiply_by_2(x):
    return 2 * x


def square(x):
    return x ** 2


def reciprocal(x):
    if x == 0:
        raise ValueError("ההופכי אינו מוגדר עבור x=0")
    return 1 / x

# : ב

def apply_functions(numbers, functions):  # ניתן להישתמש בכל פונקצייה מסעיף א'
    result = {}
    for func in functions:
        result[func.__name__] = [func(num) for num in numbers]
    return result