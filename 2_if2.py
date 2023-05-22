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

def main():

    text_1 = input('Input first string: ')
    text_2 = input('Input second string: ')

    if not text_1.isalpha() and not text_2.isalpha():
        return 0
    elif text_1 == text_2:
        return 1
    elif len(text_1) > len(text_2):
        return 2
    elif text_1 != text_2 and text_2 == 'learn':
        return 3
    else:
        return 'another variant'


if __name__ == "__main__":
    print(main())
