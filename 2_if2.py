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

def main(str1, str2):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    if type(str1) == str and type(str2) == str:
        result = 0
        if str1 == str2:
            result = 1
        elif str1 != str2:
            result = 2
        elif str2 == 'learn':
            result = 3
    else:
        result = 0

    print(result)

if __name__ == "__main__":
    main('World', 'learn')
