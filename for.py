"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

school = [{'school_class': '1a', 'scores': [3, 6, 4, 5, 1]},
          {'school_class': '2a', 'scores': [7, 4, 4, 33, 9]},
          {'school_class': '3a', 'scores': [23, 4, 4, 5, 2]},
          {'school_class': '4a', 'scores': [2, 8, 4, 5, 24]},
          {'school_class': '1b', 'scores': [3, 4, 78, 5, 42]},
          {'school_class': '2b', 'scores': [8, 12, 4, 5, 2]},
          {'school_class': '3b', 'scores': [3, 76, 4, 33, 27]},
          {'school_class': '4b', 'scores': [53, 4, 35, 5, 9]},
          ]


def main():
    all_scores = 0
    for score in school[0]["scores"]:
        all_scores += score

    print(f'средняя оценка {all_scores/ len(school[0]["scores"])}')


if __name__ == "__main__":
    main()
