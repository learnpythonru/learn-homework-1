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
def compare(first, second):
  if (type(first) == str and type(second) == str) == False:
    return 0
  elif first == second:
    return 1
  elif len(first) > len(second):
    return 2
  elif second == 'learn':
    return 3


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    

    print(compare('first',2))
    print(compare('first', 'first'))
    print(compare('longer','long'))
    print(compare('first', 'learn'))
    
if __name__ == "__main__":
    main()
