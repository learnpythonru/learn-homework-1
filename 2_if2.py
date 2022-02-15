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

def main(str_1, str_2):
    if isinstance(str_1, str) and isinstance(str_2, str):
      if str_1 == str_2:
        return '1'
      elif str_1 != str_2 and len(str_1) > len(str_2) and str_2 != 'learn':
        return '2'
      elif str_1 != str_2 and str_2 == 'learn':
        return '3'
    return '0'  
    
print(main(5, 5))
print(main('line', 'line'))
print(main('notebook', 'laptop'))
print(main('notebook', 'learn'))
print(main('learn', 'learn'))