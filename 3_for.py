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
        p = [random.randrange(1, 6, 1) for i in range(6)]
        d = {'school_class': str(i)+str(list_of_classes_in_year[k]), 'scores': p}
        a.append(d)
  return a


def middle_class_mark(i, classes, list_of_classes_in_year):
      b = []
      for k in range(len(list_of_classes_in_year)):
           b.append(str(i)+str(list_of_classes_in_year[k]))
      expectedResult = [d for d in classes if d['school_class'] in b]
      for l in range(len(expectedResult)):
         return sum(expectedResult[l]['scores']) / len(expectedResult[l]['scores'])
           


def middle_school_mark(array_of_middle):
  return sum(array_of_middle) / len(array_of_middle)

def main():

  list_of_classes = ['a','б','в','г','д']
  array_of_middle = []
  for i in range(1,12):
       middle_mark = middle_class_mark(i, generate_marks(list_of_classes), list_of_classes)
       array_of_middle.append(middle_mark)
       print('Middle mark for {0} class is {1} '.format(i, middle_mark))
  
  middle_of_school = middle_school_mark(array_of_middle)
  print('Middle mark for school {0} '.format( middle_of_school))
    
if __name__ == "__main__":
    main()
