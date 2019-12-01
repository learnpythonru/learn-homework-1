"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
import numpy


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    school_scores = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
                     {'school_class': '4b', 'scores': [5, 5, 5, 5, 2]},
                     {'school_class': '4c', 'scores': [2, 3, 4, 5, 5]}]

    # Средний балл по всей школе:

    middle = 0
    for school_class in school_scores:
        middle += sum(school_class['scores'])

    count_class = len(school_scores)
    count_score = len(school_scores[0]['scores'])
    middle_school = middle / (count_class * count_score)
    print(f'Средний балл по всей школе: {middle_school}')

    # Средний балл по каждому классу:

    for school_cl in school_scores:
        middle_class = numpy.mean(school_cl['scores'])
        school_class_name = school_cl['school_class']
        print(f'Средняя оценка по классу {school_class_name}: {middle_class}')


if __name__ == "__main__":
    main()
