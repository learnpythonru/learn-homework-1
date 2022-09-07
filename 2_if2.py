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

def lines(line1, line2):
    if isinstance(line1, str) and isinstance(line2, str):
        if line1 == line2:
            return 1
        if line1 != line2 and line2 == 'learn':
            return 3
        if line1 != line2 and len(line1) > len(line2):
            return 2

    else:
        return 0
print(lines(5, 'lel'))
print(lines('ks', 'kk'))
print(lines('Python', 'learn'))
print(lines('learn', 'ok'))
print(lines('Python', 'learn'))
