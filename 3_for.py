"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def main():
    score_count = 0
    score_sum = 0
    school_scores = [
        {'school_class': '1a', 'scores': [3, 4, 3, 5, 4]},
        {'school_class': '2a', 'scores': [3, 4, 4, 4, 5]},
        {'school_class': '3a', 'scores': [4, 5, 2, 5, 4]},
        {'school_class': '4a', 'scores': [3, 4, 4, 5, 5]},
        {'school_class': '5a', 'scores': [4, 2, 4, 5, 4]},
        {'school_class': '6a', 'scores': [3, 3, 3, 5, 5]},
        {'school_class': '7a', 'scores': [3, 4, 3, 5, 5]},
        {'school_class': '8a', 'scores': [3, 5, 5, 5, 4]},
        {'school_class': '9a', 'scores': [3, 5, 3, 5, 5]},
        {'school_class': '10a', 'scores': [3, 2, 4, 5, 5]},
        {'school_class': '11a', 'scores': [3, 5, 4, 4, 4]}
    ]
    for score in school_scores:
        print(f'Средний балл в {score["school_class"]} классе: {sum(score["scores"]) / len(score["scores"])}')
        score_sum += sum(score["scores"]) / len(score["scores"])
        score_count += 1
    print(f'Средняя балл по школе: {score_sum / score_count}')


if __name__ == "__main__":
    main()
