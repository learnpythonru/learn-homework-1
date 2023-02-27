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
    def line_comp(str1,str2):

# не строки
        if type(str1) and type(str2) != str:
            return 0

# строки одинаковые
        if str1 == str2:
            return 1

# строки разные и первая длиннее
        if str1 != str2 and len(str(str1)) > len(str(str2)):
            return 2
# строки разные и вторая строка 'learn'
        if str1 != str2 and str2 == 'learn':
            return 3

    conclusion = line_comp(1,1)
    print(conclusion)

    conclusion = line_comp('asd','asd')
    print(conclusion)

    conclusion = line_comp('asыы','asd')
    print(conclusion)

    conclusion = line_comp('asыы','learn')
    print(conclusion)



if __name__ == "__main__":
    main()
