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


def main(s1, s2):
    if not isinstance(s1, str) or not isinstance(s2, str):
        return 0
    elif s1 == s2:
        return 1
    elif s1 != s2 and len(s1) > len(s2):
        return 2
    else:
        return 3


if __name__ == "__main__":
    print(main("learn", "mom"))
    print(main("father", "learn"))
    print(main(123, "learn"))
    print(main("learn", "learn"))
    print(main("mom", "learn"))