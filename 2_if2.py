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

def check_string(first_string, second_string):
    if not isinstance(first_string, str) or not isinstance(second_string, str):
        return 0
    elif first_string == second_string:
        return 1
    elif second_string == 'learn':
        return 3
    elif len(first_string) > len(second_string):
        return 2

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(check_string('python', 2))
    print(check_string('python', 'python'))
    print(check_string('python', 'js'))
    print(check_string('python', 'learn'))

if __name__ == "__main__":
    main()
