"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
school = [
    {'school_class': '4a', 'scores': [3,3,5,5,2,5,5,2]},
    {'school_class': '4b', 'scores': [4,4,3,5,4,5,4]},
    {'school_class': '5a', 'scores': [3,5,5,2,4,3,3,3,3]}, 
    {'school_class': '5b', 'scores': [5,5,5,5,3]},
    {'school_class': '6a', 'scores': [2,4,4]},
    {'school_class': '6b', 'scores': [5,3,2,5]},
    {'school_class': '7a', 'scores': [4,5,4,2,2,3,5]},
    {'school_class': '7b', 'scores': [2,2,5,4]},
    {'school_class': '8a', 'scores': [4,5,3,4,3]},
    {'school_class': '8b', 'scores': [2,4,2,3,4,5,5,3,3,5]},
    {'school_class': '9a', 'scores': [2,2,2,2,2,3,4]},
    {'school_class': '9b', 'scores': [4,3,3,3,3]}
    ]


def main(school):
    gen_scores = []
    for school_class in school:
        scores_class = sum(school_class.get('scores')) / len(school_class.get('scores'))
        gen_scores.append(scores_class)
    return gen_scores


print('Средний балл по школе: ', sum(main(school))/len(school), '\nСредний балл по классам: ', main(school))
