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

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    first_string = input()
    second_string = input()
    if not type(first_string or second_string) is str:
        print('0')
    elif first_string == second_string:
        print('1')
    elif first_string != second_string and first_string > second_string:
        print('2')
    elif first_string != second_string and second_string == 'learn':
        print('3')
    else:
        print('''Let's try again''')

if __name__ == "__main__":
    main()
