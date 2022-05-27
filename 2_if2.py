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
first = input()
second = input()
def function(first, second):
  if type(first) == int and type(second) == int:
    print('0')
  elif first == second:
    print('1')
  elif first != second and second == "learn":
    print('3')
  elif first != second and len(first) > len(second):
    print('2')      

function(1, 5)
function('fdf', 'fdf')
function('hxckhxzc', 'ckjdc')
function('vnj', 'learn')


if __name__ == "__main__":
    main()