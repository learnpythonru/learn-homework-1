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


def check_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        return 0

    str1 = str1.strip().lower()
    str2 = str2.strip().lower()

    if str1 == str2:
        return 1
    elif str2 == 'learn':
        return 3
    elif len(str1) > len(str2):
        return 2
    else:
        return 'Вот это поворот'


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    print(check_strings('hello', 777))  # 0
    print(check_strings('hello', 'hello'))  # 1
    print(check_strings('hello', 'hell'))  # 2
    print(check_strings('hi', 'learn'))  # 3
    print(check_strings('hi', 'learning'))


if __name__ == "__main__":
    main()
