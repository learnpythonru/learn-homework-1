"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

scores_table = [
    {'school_class': '1а',
     'scores': [3, 4, 5, 5, 4, 3, 4]
     },
    {'school_class': '2б',
     'scores': [4, 4, 3, 2, 4, 5]
     },
    {'school_class': '3б',
     'scores': [2, 4, 5, 3, 3, 4]
     },
    {'school_class': '4в',
     'scores': [3, 5, 5, 4, 5, 4, 5]
     },
]


def get_average(scores):
    summary = 0
    for score in scores:
        summary += score
    return summary / len(scores)


def main():
    avg_by_school = []
    for class_table in scores_table:
        avg_by_class = get_average(class_table["scores"])
        print(f'Class: {class_table["school_class"]}, Avg score: {round(avg_by_class, 2)}')
        avg_by_school.append(avg_by_class)
    print('----------------------------')
    print(f'Avg score by school: {round(get_average(avg_by_school), 2)}')


if __name__ == "__main__":
    main()
