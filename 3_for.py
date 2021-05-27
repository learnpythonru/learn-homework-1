"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

import random


def generate_marks(list_of_classes_in_year) -> list:
  a = []
  for i in range(1,12):
    for k in range(len(list_of_classes_in_year)):
        p = [random.randrange(1, 6, 1) for _ in range(6)]
        d = {'school_class': str(i)+str(list_of_classes_in_year[k]), 'scores': p}
        a.append(d)
  return a


def middle_school_mark(array_of_middle):
  return sum(array_of_middle) / len(array_of_middle)


def main():

  list_of_classes = ['a','б','в','г','д']
  classes = generate_marks(list_of_classes)
  array_of_marks = []

  expectedResult = [d for d in classes if d['school_class']]
  for l in range(len(expectedResult)):
         array_of_marks = array_of_marks + expectedResult[l]['scores']
         middle = sum(expectedResult[l]['scores']) / len(expectedResult[l]['scores'])
         print('Middle mark for {0} class is {1} '.format(expectedResult[l]['school_class'], middle))
 
  middle_school = middle_school_mark(array_of_marks)
  print('Middle mark for school {0} '.format(middle_school))
if __name__ == "__main__":
    main()
