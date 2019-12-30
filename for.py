"""
Домашнее задание №1
Цикл for: Оценки
* Создать список из словарей с оценками учеников разных классов
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
from random import randint, choice
from statistics import mean

CLASS = int(input('How many classes in school: > '))
LETTER = ['a', 'b', 'c', 'd', 'e']


def students_score():
    """
    scores = список оценок от 2 бало до 5, который возвращает функция
    :return:
    """
    scores = [randint(2, 5) for i in range(5)]
    return scores


def class_and_scores():
    # Случайным образом выбираем классы и генерируем в них балы.
    school_student = [{'school_class': str(i) + choice(LETTER), 'scores': students_score()} for i in
                      range(1, CLASS + 1)]
    return school_student


def mid_score_in_school(score_list):
    mid_school = [mean(item['scores']) for item in score_list]
    print('Средний бал в школе: {}\n'.format(mid_school))


def mid_score_per_class(score_list):
    for item in score_list:
        print(item['school_class'], item['scores'])
        print('Сумма всех оценок в {} классе: {}'.format(item['school_class'], sum(item['scores'])))
        print('Средний бал по {} классу = {}\n'.format(item['school_class'], mean(item['scores'])))


def main():
    class_and_scores()

    # средний балл по всей школе.
    mid_score_in_school(class_and_scores())

    # средний балл по классам.
    mid_score_per_class(class_and_scores())


if __name__ == "__main__":
    main()
