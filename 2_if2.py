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
first_string = 'pidor'
second_string = 'learn'
def compare_string(first_string, second_strin):
    if isinstance(first_string, str) and isinstance(second_strin, str):
    # if isinstance(first_string, str):
        print(0)
    elif first_string == second_string:
        print(1)
    elif first_string != second_string and first_string > second_string:
        print(2)
    elif first_string != second_string and second_string == 'learn':
        print(3)
    else:
        print('''Let's try again''')

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    compare_string(first_string, second_string)


if __name__ == "__main__":
    main()
