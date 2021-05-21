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
 тест
"""
def string_compare(str1, str2):
  first_string = str(str1)
  second_string = str(str2)
  if first_string.isalpha() and second_string.isalpha():
    if first_string == second_string:
      return 1
    elif first_string != second_string and len(first_string) > len(second_string):
      return 2
    elif first_string != second_string and second_string == 'learn':
      return 3
  else:
    return 0  


def main():
    
    str1, str2 = input(), input()
    print(string_compare(str1, str2))
    
if __name__ == "__main__":
    main()
