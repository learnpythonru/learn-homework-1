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

def main(line1, line2):
    if (isinstance(line1, str)) and (isinstance(line2, str)):    #проверка, являются ли строки - строками
       print(f'Проверка: "{line1}" и "{line2}" - являются строками') 
    else:
        return 0
    if len(line1) == len(line2):
        return 1
    elif len(line1) > len(line2):
            return 2
    elif len(line1) != len(line2) and line2 == 'learn':
        return 3
    else:
        return None
if __name__ == "__main__":

    print(main(123, 'строка'))
    print(main(123, 3332))
    print(main('строка', 123))
    print(main("равные", "строки"))
    print(main('learn', 'learn'))
    print(main('длиннее', 'короче'))
    print(main('длиннее', 'learn'))
    print(main('abc', 'learn'))