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
def compare_string(string_one, string_two):
    if type(string_one) != type('str') or type(string_two) != type('str'):
        return 0
    elif string_one == string_two:
        return 1
    elif len(string_one) > len(string_two):
        return 2
    elif string_two == 'learn':
        return 3
    else:
        return 'Норм'


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(compare_string('1', '2'))
    print(compare_string(1, '2'))
    print(compare_string('1', 2))
    print(compare_string([], '2'))
    print(compare_string('kjdfklsdjf', 'sldksl'))
    print(compare_string('asd', 'dskjfklj'))
    print(compare_string('asd', 'learn'))
    print(compare_string('learn', 'learn'))
    
if __name__ == "__main__":
    main()
