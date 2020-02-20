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


def check_line(line_one: str, line_two: str) -> int:
    if not (isinstance(line_one, str) and isinstance(line_two, str)):
        return 0
    elif line_one == line_two:
        return 1
    elif line_one != line_two and len(line_one) > len(line_two):
        return 2
    elif line_one != line_two and line_two == 'learn':
        return 3


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    line_one = [1, 2, 3]
    line_two = [2]
    print(check_line(line_one, line_two))


if __name__ == "__main__":
    main()
