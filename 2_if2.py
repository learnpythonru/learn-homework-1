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


def check_strings(str1, str2):
    if not (type(str1) is str and type(str2) is str):
        return 0
    elif str1 == str2:
        return 1
    elif len(str1) > len(str2):
        return 2
    elif str2 == 'learn':
        return 3
    else:
        return 4


def main():
    print(check_strings(0, 0))               # both arguments are not strings
    print(check_strings(0, 'test'))          # first argument is not a string
    print(check_strings('test', 'test'))     # the strings are equal
    print(check_strings('test123', 'test'))  # the first string is longer than second one
    print(check_strings('test', 'learn'))    # the second string is 'learn'
    print(check_strings('test', 'test123'))  # the second string is longer than first one (fallback value is 4)
    print(check_strings('test1', 'test2'))   # two different strings with equal length (fallback value is 4)


if __name__ == "__main__":
    main()
