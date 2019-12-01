"""
Домашнее задание №1
Цикл for: Оценки
* Создать список из словарей с оценками учеников разных классов
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
from random import randint, choice

CLASS = int(input('How many classes in school: > '))
LETTER = ['a', 'b', 'c', 'd', 'e']


def students_score():
    """
    scores = список оценок от 2 бало до 5, который возвращает функция
    :return:
    """
    scores = [randint(2, 5) for i in range(5)]
    return scores


def main():
    school_student = []  # {'school_class': '1a', 'scores': students_score()}

    # Случайным образом выбираем классы и генерируем в них балы.
    school_student = [{'school_class': str(i) + choice(LETTER), 'scores': students_score()} for i in range(1, CLASS + 1)]

    # Посчитать и вывести средний балл по всей школе.
    mid_school = [sum(item['scores']) / len(item['scores']) for item in school_student]
    mid_score = sum(mid_school) / len(mid_school)
    print('Средний бал в школе: {}\n'.format(mid_score))

    # Посчитать и вывести средний балл по классам.
    for item in school_student:
        print(item['school_class'], item['scores'])
        print('Сумма всех оценок в {} классе: {}'.format(item['school_class'], sum(item['scores'])))
        print('Средний бал по {} классу = {}\n'.format(item['school_class'], sum(item['scores']) / len(item['scores'])))


if __name__ == "__main__":
    main()
