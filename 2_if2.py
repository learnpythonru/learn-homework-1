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
def some_checking(condition_1, condition_2):
  if type(condition_1) != type(condition_2) is not str: #Данное условие игнорируется :(
      return 0
  elif condition_1 == condition_2:
      return 1 
  elif len(condition_1) > len(condition_2):
      return 2
  elif condition_2 == 'learn':
      return 3
  else:
      return "Данного условия нет!"


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    
    condition_1 = input('Попробуйте ввести первое условие: ')
    condition_2 = input('Попробуйте ввести второе условие: ')
    new_condition = some_checking(condition_1, condition_2)
    print(new_condition)

    
if __name__ == "__main__":
    main()
