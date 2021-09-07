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


def main(str_1, str_2):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if type(str_1) != str or type(str_2) != str:
        return 0
    elif str_1 == str_2:
        return 1
    elif str_1 != str_2 and str_2 == 'learn':
        return 3
    elif str_1 != str_2 and len(str_1) > len(str_2):
        return 2


if __name__ == "__main__":
    string_1 = 0
    string_2 = 0
    result = main(string_1, string_2)
    print(result)

    string_1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    string_2 = 0
    result = main(string_1, string_2)
    print(result)

    string_1 = 0
    string_2 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    result = main(string_1, string_2)
    print(result)

    string_1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    string_2 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    result = main(string_1, string_2)
    print(result)

    string_1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    string_2 = 'Ut non nisi neque. Phasellus sit amet varius leo.'
    result = main(string_1, string_2)
    print(result)

    string_1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    string_2 = 'learn'
    result = main(string_1, string_2)
    print(result)
