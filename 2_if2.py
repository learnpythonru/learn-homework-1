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


def check_strings(firs_str, second_str):
    firs_str = firs_str.lower()
    second_str = second_str.lower()
    if isinstance(firs_str and second_str, str):
        if firs_str == second_str:
            return 1
        else:
            if firs_str > second_str and second_str != 'learn':
                return 2
            elif second_str == 'learn':
                return 3
            else:
                return 'Нет в условии'
    else:
        return 0


def main():
    print(check_strings('f', 'LEARN'))


if __name__ == "__main__":
    main()

