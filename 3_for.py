"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.

1. Объявить переменную с оценками для каждого класса
2. Посчитать средний балл по каждому классу и записать результаты в переменную (список/словарь)
3. Передать результаты по классам в функцию подсчета среднего и вывести результаты

1. How to calc avg for a list elements?
2. How to use only 'scores' value
"""


def calc_avg(marks):
    avg_marks_value = sum(marks)/len(marks)
    return avg_marks_value


def main():
    pass


if __name__ == "__main__":
    marks = [{'school_class': '1a', 'scores': [3, 4, 2, 5, 2]},
             {'school_class': '2a', 'scores': [3, 3, 4, 5, 2]},
             {'school_class': '3a', 'scores': [3, 4, 4, 1, 2]}]
    avg_marks = []
    for mark in marks:
        scores = mark['scores']
        avg_value = calc_avg(scores)
        print('Results for class {1} = {0}'.format(avg_value, mark['school_class']))
        avg_marks.append(avg_value)
    avg_school_value = calc_avg(avg_marks)
    print('The average score for the whole school {0}' .format(round(avg_school_value,1)))



