"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

import random
import itertools
from pprint import pprint


def generate_data():

    literals = ['a', 'b', 'c']
    digits = range(1, 11, 1)
    classes = []
    c = list(itertools.product(digits, literals))
    for each in c:
        classes.append(str(each[0]) + str(each[1]))

    student_scores = []
    for cls in classes:
        scores = [random.randint(1, 5) for i in range(random.randint(10, 20))]
        current_class_dict = {'school_class': cls, 'scores': scores}
        student_scores.append(current_class_dict)

    return student_scores


def get_class_mean(current_class):
    """
    функция вычисляет средний балл по переданному ей классу школы\
    """

    class_scores = sum(current_class['scores'])
    class_students = len(current_class['scores'])
    class_mean = class_scores / class_students
    return class_mean


def get_school_mean(student_scores):
    scores_sum = 0
    students = 0
    for cls in student_scores:
        class_sum = sum(cls['scores'])
        class_students = len(cls['scores'])
        scores_sum += class_sum
        students += class_students
    return round(scores_sum / students, 2)


def get_school_mean_v2(school_scores):
    """
    если научиться сразу читать задание целиком, а не по пунктам, то можно было бы понять, что
    второй пункт можно сделать частью первого
    """

    class_counts = 0
    scores_sum = 0
    for cls in school_scores:
        scores_sum += get_class_mean(cls)
        class_counts += 1
    return round(scores_sum / class_counts, 2)


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    student_scores = generate_data()
    # pprint(student_scores)
    print(f'Средний балл по школе {get_school_mean(student_scores)} - вариант 1')
    print(f'Средний балл по школе {get_school_mean_v2(student_scores)} - вариант 2')

    for cls in student_scores:
        print(f"Средний балл класса: {cls['school_class']} - {round(get_class_mean(cls), 2)}")


if __name__ == "__main__":
    main()
