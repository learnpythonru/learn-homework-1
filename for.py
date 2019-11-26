"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    scores = [
        {'school_class': '4a', 'scores': [3,4,4,5,3,4,4,5]},
        {'school_class': '4b', 'scores': [5,4,4,5,3,5,4,4,3]},
        {'school_class': '4c', 'scores': [3,4,4,5,2,4,3]},
        {'school_class': '4d', 'scores': [3,4,5,3,3,3,5,5]},
        {'school_class': '4e', 'scores': [4,4,3,5,4,4,5,5,4,3]},
    ]

# средний балл по школе
    scores_sum = 0
    school_cnt = 0
    for school_class in scores:
        for score in school_class['scores']:
            scores_sum += score
        school_cnt += len(school_class['scores'])
    print('Средний балл по школе: {}'.format(scores_sum / school_cnt))
    print('')
    print('* Cредний балл по каждому классу *')
# средний балл по каждому классу
    for school_class in scores:
        class_cnt = 0
        for score in school_class['scores']:
            class_cnt += score
        school_class['scores_avg'] = class_cnt / len(school_class['scores'])

# вывод результатов
    print('Класс\tСредний балл')
    for school_class in scores:
        print('{}\t{}'.format(school_class['school_class'], school_class['scores_avg']))

if __name__ == "__main__":
    main()
