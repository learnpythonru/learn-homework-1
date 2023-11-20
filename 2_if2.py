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


def string_comparison():
    text_1 = input("Введите первую строку: ")
    text_2 = input("Введите вторую строку: ")
    if not (isinstance(text_1, str) or isinstance(text_1, str)):
        return print(0)
    if (text_1) == (text_2):
        return print(1)
    if len(text_1) > len(text_2):
        return print(2)
    if text_2 == "learn":
        return print(3)


def main():
    total = int(input("Укажите количество проверок: "))
    for _ in range(total):
        string_comparison()


if __name__ == "__main__":
    main()
