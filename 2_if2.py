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


def compare_strings(string_1: str, string_2: str) -> int:
    if not all([isinstance(string_1, str), isinstance(string_2, str)]):
        return 0
    elif string_1 == string_2:
        return 1
    elif len(string_1) > len(string_2) and string_2 != 'learn':
        return 2
    elif string_1 != string_2 and string_2 == 'learn':
        return 3


def main():
    print(compare_strings(1, 'string'))
    print(compare_strings('string', 'string'))
    print(compare_strings('strings', 'string'))
    print(compare_strings('string', 'learn'))
    print(compare_strings('learn', 'string'))


if __name__ == "__main__":
    main()
