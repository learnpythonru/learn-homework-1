"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3ы
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
first_string = input()
second_string = input()
def main():
    
    def string_comparator(first_string,second_string):
      if first_string == second_string:
          return 1
      elif len(first_string) > len(second_string):
          return 2
      elif second_string == 'learn':
          return 3

    
if __name__ == "__main__":
    main()
