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

def main(string_1, string_2):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    #if not(type(string_1) == str and type(string_2) == str):
    if not isinstance(string_1, str) or not isinstance(string_2, str):
      return 0
    elif string_1 == string_2:
      return 1
    elif len(string_1) > len(string_2):
      return 2
    elif string_2 == 'learn':
      return 3 

    
if __name__ == "__main__":
    print(main(25, 'checking'))
    print(main('learn', 'learn'))
    print(main('nothing to', 'do'))
    print(main('nothing to', 'learn'))
    print(main('cat', 'learn'))

