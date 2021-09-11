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


def main(string, string2):
    if not (isinstance(string, str) and isinstance(string2, str)):
        return 0
    elif len(string) == len(string2):
        return 1
    elif string2 == 'learn':
        return 3
    elif len(string) > len(string2):
        return 2


if __name__ == "__main__":
    print(main(1, 2))
    print(main("привет", 2))
    print(main("hello", "привет"))
    print(main("Пойдём", "Гулять"))
    print(main("learn", "learn"))
    print(main("lesson", "Learn"))
    print(main("Python", "learn"))
