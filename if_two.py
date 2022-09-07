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

def compare_two_strings(line1, line2):
    if type(line1) != str or type(line2) != str:
        return 0

    if line1 == line2:
        return 1

    if len(line1) > len(line2) and line2 != 'learn': #если убрать второе условие, 3 не вернется при line1 > line2
        return 2

    if line2 == 'learn':
        return 3

    return 'подходящих условий не нашлось'
    
if __name__ == "__main__":
    line1 = '2'
    line2 = 2
    print(compare_two_strings(line1, line2))

    line1 = 'remove'
    line2 = 'remove'
    print(compare_two_strings(line1, line2))

    line1 = 'very long'
    line2 = 'short'
    print(compare_two_strings(line1, line2))

    line1 = 'Python'
    line2 = 'learn'
    print(compare_two_strings(line1, line2))