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

def strings(st1, st2):

    if not isinstance(st1, str) or not isinstance(st2, str):
      return 0
    else:

      if st1 == st2:
        return 1

      elif st1 != st2 and st2 == "learn":
        return 3

      elif st1 != st2 and len(st1) > len(st2):
        return 2

print(strings(st1 = 'four', st2 = 'two')) #2
print(strings(1, 10)) #0
print(strings('one', 'one')) #1
print(strings('ананас', 'learn')) #3
