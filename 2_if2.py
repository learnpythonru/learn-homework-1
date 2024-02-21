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


def check_two_strings(first_string: str, second_string: str) -> int:
    if type(first_string) != str or type(second_string) != str:
        return 0
    if first_string == second_string:
        return 1
    if len(first_string) > len(second_string):
        return 2
    if first_string != second_string and second_string == 'learn':
        return 3


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(check_two_strings('s', 5))
    print(check_two_strings('s', 's'))
    print(check_two_strings('spk', 's'))
    print(check_two_strings('s', 'learn'))


if __name__ == "__main__":
    main()
