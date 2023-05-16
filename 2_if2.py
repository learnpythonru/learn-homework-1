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


def main(a=input('Please, enter first value: '),
         b=input('Please, enter second value: ')):

    types: str = f'a={a}(type={type(a).__name__}), b={b}(type={type(b).__name__}))'

    if not isinstance(a, str) or not isinstance(b, str):
        print('0', types, sep=', ')
    else:
        if a == b:
            print('1', types, sep=', ')
        else:
            if len(a) > len(b):
                print('2', types, sep=', ')
            elif b == 'learn':
                print('3', types, sep=', ')
            else:
                print('No such condition', types, sep=', ')


if __name__ == "__main__":
    tests: list = [
        ['123', '123'],                     # str: equal length
        ['1234', '123'],                    # str: length a > length b
        ['123', '1234'],                    # str: length a < length b
        ['123', 'learn'],                   # str: b == 'learn'
        [123, 321],                         # int: 2 integers
        ['123', 123],                       # int: 1 integer
        [1.2, 55.5],                        # float: 2 floats
        ]

    main()                                  # manual input
    [main(i[0], i[1]) for i in tests]       # tests
