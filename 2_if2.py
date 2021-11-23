"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные параметры 
  и выводя на экран результаты

"""


def parse_strings(first_str, second_str):
  if type(first_str) != str or type(second_str) != str:
    return 0
  if first_str == second_str:
    return 1
  if first_str != second_str and second_str == 'learn':
    return 3
  if len(first_str) > len(second_str):
    return 2


def main():
  args = [
      [{}, 2], 
      [1, 'str'], 
      [True, 'str'], 
      [list(), ValueError()], 
      ['equalstr', 'equalstr'], 
      ['strlonger', 'str'], 
      ['strlonger', 'learn'], 
      ['learn', 'learn']
    ]

  for data in args:
    print(f"Input: {data}\n  Result: {parse_strings(data[0], data[1])} \n")


if __name__ == "__main__":
    main()
