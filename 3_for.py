from itertools import product
from random import randrange
from statistics import mean
"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
def get_school_classes(grades_count, liters):
    classes = [grade for grade in range(1, grades_count + 1)]
    school_classes = product(classes, liters)
    school_classes = [
        f'{school_class}{liter}' for school_class, liter in school_classes
        ]
    return school_classes


def get_classes_data(school_classes):
    highest_mark = 5
    marks_count = 6
    classes_data = {}
    for school_class in school_classes:
        classes_data['school_class'] = school_class
        classes_data['scores'] = [
            randrange(1, highest_mark +1) for score in range(marks_count)
            ]
        yield classes_data


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    grades_count = 11
    liters = ['a', 'b', 'c']
    mean_scores = []

    school_classes = get_school_classes(grades_count, liters)
    classes_data = get_classes_data(school_classes)

    for school_class in classes_data:
        mean_score = mean(school_class["scores"])
        print(f'Средняя оценка {school_class["school_class"]}'
            f' - {mean_score}')
        mean_scores.append(mean_score)

    overall_mean_score = mean(mean_scores)

    print(f'Средний балл по школе - {overall_mean_score}')


if __name__ == '__main__':
    main()
