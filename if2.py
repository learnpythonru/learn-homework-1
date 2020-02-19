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

def string_comparison(str_1, str_2):
    if type(str_1) is not str and type(str_2) is not str:
        return 0
    elif str_1 == str_2:
        return 1
    elif str_1 != str_2 and len(str_1) > len(str_2):
        return 2
    elif str_1 != str_2 and str_2 == 'learn':
        return 3

print(string_comparison(1, 3))
print(string_comparison('python', 'python'))
print(string_comparison('learn python well', 'good'))
print(string_comparison('study', 'learn'))



    
if __name__ == "__main__":
    main()
