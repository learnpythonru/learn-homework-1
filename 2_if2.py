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
running = True


def main(line_1, line_2):
    if type(line_1) != str and type(line_2) != str:
        print(0)
    elif len(line_1) == len(line_2) and line_2 != 'learn':
        print(1)
    elif len(line_1) > len(line_2):
        print(2)
    elif len(line_1) != len(line_2) and line_2 == 'learn':
        print(3)
    else:
        print('неизвестно')


while running:
    line_1 = input('Введите первую строку: ')
    line_2 = input('Введите вторую строку: ')
    if line_1 == 'STOP':
        break
    elif line_2 == 'STOP':
        break
    else:
        main(line_1, line_2)
