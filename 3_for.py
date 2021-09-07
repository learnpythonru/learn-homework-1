"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def main(data):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    average_school_score = 0
    for classroom in data:
        classroom['average_class_score'] = sum(classroom['scores']) / len(classroom['scores'])
        average_school_score += classroom['average_class_score']
    return average_school_score, data


if __name__ == "__main__":
    school = [
        {'school_class': '1а',
         'scores': [2, 3, 3, 4, 5]
         },
        {'school_class': '1б',
         'scores': [2, 4, 3, 1, 3]
         },
        {'school_class': '2a',
         'scores': [3, 3, 4, 2, 5]
         },
        {'school_class': '2б',
         'scores': [1, 1, 2, 3, 2]
         },
        {'school_class': '3a',
         'scores': [1, 1, 1, 3, 3]
         },
        {'school_class': '3б',
         'scores': [5, 5, 1, 1, 3]
         },
        {'school_class': '4a',
         'scores': [2, 1, 1, 3, 4]
         },
        {'school_class': '4б',
         'scores': [3, 3, 2, 3, 1]
         }
    ]

    average_score, results = main(school)
    print(f'Средний балл по всей школе: {round(average_score, 2)}')
    for result in results:
        print(f'Средний балл в {result["school_class"]}: {result["average_class_score"]}')
