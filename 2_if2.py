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
    if type(string) != str and type(string2) != str:
        return 0
    elif string == string2:
        return 1
    elif len(string) > len(string2):
        return 2
    elif string2 == 'learn':
        return 3


if __name__ == "__main__":
    string = input()
    string2 = input()
    compare = main(string, string2)
    print(compare)
