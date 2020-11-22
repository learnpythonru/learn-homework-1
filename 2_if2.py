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

    def compare_2_strings(str1, str2):
        if (type(str1) != str) or (type(str2) != str):
            return 0
        elif str1 == str2:
            return 1
        elif str1 != str2 and len(str1) > len(str2):
            if str2 == 'learn':
                return 3
            return 2
        elif str1 != str2 and str2 == 'learn':
            return 3

    print(compare_2_strings(1, 'pdsfsfsfs'))
    print(compare_2_strings('pdsfsfsfs', 312))
    print(compare_2_strings('sreee', 'sreee'))
    print(compare_2_strings('sreee32424', 'tr3eee'))
    print(compare_2_strings('Skr', 'skreee'))  # По условию не проходит)
    print(compare_2_strings('Skr', 'learn'))
    print(compare_2_strings('qeqedsd', 'learn'))
    print(compare_2_strings(123, 'learn'))
    print(compare_2_strings('learn', 'sdsdar'))  # По условию не проходит)


if __name__ == "__main__":
    main()
