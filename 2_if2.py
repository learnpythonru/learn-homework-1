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

#вопрос что делать если это строки разной длины и вторая не learn?

import random


def is_it_strings(str1, str2):
    if not (isinstance(str1, str) and isinstance(str2, str)):
        return 0
    else:
        if str1 == str2:
            return 1
        elif len(str1) > len(str2):
            return 2
        elif 'learn' == str2:
            return 3


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    strings = ['learn', 'python', 'some', 'words', 3, 5, 7, {'name': 1}]

    for i in range(20):
        str1 = random.choice(strings)
        str2 = random.choice(strings)
        print(is_it_strings(str1, str2))

    # print('some', 'words', is_it_strings('some', 'words'))


if __name__ == "__main__":
    main()
