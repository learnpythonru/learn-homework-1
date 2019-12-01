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


def two_string_func(string_1, string_2):
    if isinstance(string_1, str) and isinstance(string_2,
                                                str):  # Проверить, является ли то, что передано функции, строками.
        result = 'This is a string'
        print(result)
        if string_1 == string_2:  # Если строки одинаковые, вернуть 1
            number = 1
            return number
        elif len(string_1) > len(string_2):  # Если строки разные и первая длиннее, вернуть 2
            number = 2
            return number
        elif string_1 != string_2 and string_2 == 'learn':  # Если строки разные и вторая строка 'learn', возвращает 3
            number = 3
            return number


    else:
        number = 0
        return number


def main():
    value = two_string_func('143', 'learn')
    print(value)


if __name__ == "__main__":
    main()
