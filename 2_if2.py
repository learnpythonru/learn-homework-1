"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные параметры
  и выводя на экран результаты

"""


def main(string1, string2):
    # Является ли то, что передано функции, строками
    if isinstance(string1, str) and isinstance(string2, str):
        # Если строки разные
        if string1 != string2:
            # Если вторая строка 'learn', возвращает 3
            if string2 == 'learn':
                return 3
            # Если первая длиннее, вернуть 2
            elif string1 != string2 and len(string1) > len(string2):
                return 2
            # В условии не сказано, что выводить в данному случае, поэтому, пусть будет так
            else:
                return 'Строки разные'
        else:
            return 1
    # Иначе - вернуть 0
    else:
        return 0


if __name__ == "__main__":
    print(main('python', 'learn'))
    print(main('hello', 'hello'))
    print(main(2, 6))
    print(main('trololo', 1))
    print(main(1, 'trololo'))
    print(main('trololo', 'hi'))
    print(main('hi', 'trololo'))
