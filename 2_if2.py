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
    if (type(line1) != str or type(line2) != str):
        return print('0')
    elif line1 == line2:
        return print("1")
    elif line1 != line2 and len(line1) > len(line2):
        return print("2")
    elif line1 != line2 and line2 == "learn":
        return print("3")
    else:
        print("")

main("learn", 0)
main("learn", "learn")
main("learnt", "learn")
main("does", "learn")