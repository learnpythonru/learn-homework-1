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
def compare_str(str0,str1) -> int:
    if type(str0) != str or type(str1) != str:
        return 0
    elif str0 != str1 and str1 == 'learn':
        return 3
    elif str0 != str1 and len(str0)>len(str1):
        return 2
    else: return 1
    
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    
    print(compare_str(1,2))
    print(compare_str(1,'hello'))
    print(compare_str('hello','hello'))
    print(compare_str('hello_world','hello'))
    print(compare_str('hello_world','learn'))
    
if __name__ == "__main__":
    main()
