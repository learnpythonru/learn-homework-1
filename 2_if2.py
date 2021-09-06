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

def main(first_str, second_str):
    if type(first_str)!=str and type(second_str)!=str:
        print(0)
    elif first_str == second_str:
        print(1)
    elif (first_str != second_str) and second_str=='learn':
        print(3)
    elif len(first_str) > len(second_str):
        print(2)

main(1,3)
main('hello','hello')
main('new','ne')
main('py2','learn')

