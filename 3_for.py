"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

classes = [{'school_class': '4a', 'scores': [5, 4, 4, 5, 3]},
           {'school_class': '4б', 'scores': [4, 2, 5, 5, 3]},
           {'school_class': '4в', 'scores': [4, 4, 5, 2, 3]},
           {'school_class': '4г', 'scores': [4, 4, 5, 5, 3]},
           {'school_class': '5а', 'scores': [5, 4, 5, 5, 5]},
           {'school_class': '5б', 'scores': [2, 4, 5, 3, 3]},
           {'school_class': '5в', 'scores': [4, 4, 5, 4, 3]},
           {'school_class': '5г', 'scores': [3, 2, 5, 4, 5]}]


def main():
    sum_gpa_cls = 0
    for i in classes:
        sum_gpa_cls += sum(i['scores']) / len(i['scores'])
    gpa_school = sum_gpa_cls / len(classes)
    print(f'СРЕДНИЙ БАЛЛ ПО ШКОЛЕ: {gpa_school}')
    for i in classes:
        print(f'Средний балл по классу "{i["school_class"]}":'
              f' {sum(i["scores"])/len(i["scores"])}')


if __name__ == "__main__":
    main()
