"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты
"""


def compare_two_strings(str1, str2):
    if not (isinstance(str1, str) and isinstance(str2, str)):
        return 0
    elif str1 == str2:
        result = 1
    elif len(str1) > len(str2):
        result = 2
    elif str2 == "learn":
        result = 3
    else:
        # непонятно, что делать, если str2 > str1 и str2 != 'learn'
        result = None
    return result


def main():
    print(compare_two_strings('string', {'one': 1}))
    print(compare_two_strings(0, 1))
    print(compare_two_strings([], 'string'))
    print(compare_two_strings('equal', 'equal'))
    print(compare_two_strings('this string is longer', 'qwerty'))
    print(compare_two_strings('lrn', 'learn'))
    print(compare_two_strings('now', 'second string is longer'))


if __name__ == "__main__":
    main()
