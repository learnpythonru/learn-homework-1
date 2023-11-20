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
def two_strings(one, two):
    a = isinstance(one, str)
    b = isinstance(two, str)
    if a and b:
      if one == two:
          return 1
      elif two == 'learn':
          return 3
      elif len(one) > len(two):
          return 2
      else:
          pass
    else:
        return 0


def main():
    print(two_strings('hfp','hfp'))
    print(two_strings('hfpsdf','hfp'))
    print(two_strings('lkj',1))
    print(two_strings(4,4))
    print(two_strings('sdfsfds','learn'))

    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    #pass
    
if __name__ == "__main__":
    main()
