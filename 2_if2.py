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


def main(str_one, str_two):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    if type(str_one) != str and type(str_two) != str:
        print(0)
    elif str_one == str_two:
        print(1)
    elif str_one != str_two and len(str_one) > len(str_two):
        print(2)
    elif str_one != str_two and str_two == "learn":
        print(3)


if __name__ == "__main__":
    main(1, 2)

if __name__ == "__main__":
    main("python", "python")

if __name__ == "__main__":
    main("learn_python", "python")

if __name__ == "__main__":
    main("py", "learn")
