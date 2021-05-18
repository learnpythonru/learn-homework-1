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
def string_comparison(string1, string2):
    if string1 == str(string1) and string2 == str(string2):
        if string1 == string2:
            return 1
        elif string1 != string2 and len(string1) > len(string2):
            return 2
        elif string1 != string2 and string2 == 'learn':
            return 3
    else:
        return 0


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(string_comparison(1, 'message'))
    print(string_comparison('Python', 'learn'))
    print(string_comparison('Function', 'Function'))
    print(string_comparison('main', 'learn'))
    
if __name__ == "__main__":
    main()
