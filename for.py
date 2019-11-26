"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def avg_scores(school_classes):
    sum_of_class = 0
    sum_of_school = 0
    number_of_scores = 0
    for school_class in school_classes:
        for score in school_class.get('scores'):
            sum_of_class += score
            sum_of_school += score
        number_of_scores += len(school_class.get('scores')) 
        print("Средний балл в классе \"", school_class.get('school_class'), 
        "\" - ",sum_of_class/len(school_class.get('scores'))  ,sep = "")
        sum_of_class = 0
    print("Средний балл по школе:", sum_of_school/number_of_scores)      


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school_classes = [
        {'school_class': '1',    'scores': [1,2,3,4,5]}, #15 15 3
        {'school_class': '2',    'scores': [2,2,2,2,2]}, #10 25 2
        {'school_class': '3',    'scores': [3,3,3,3,3]}, #15 40 3
        {'school_class': '5',    'scores': [4,4,4,4,4]}, #20 60 4
        {'school_class': '6',    'scores': [5,1,2,3,4]}, #15 75 3
        {'school_class': '7',    'scores': [5,5,5,5,5]}, #25 100 5
        {'school_class': '8',    'scores': [3,3,3,3,3]}, #15 115 3
        {'school_class': '9-1',  'scores': [3,4,5,5,5]}, #22 137 4.4
        {'school_class': '10-1', 'scores': [4,5,2,5,5]}, #21 158 4.2
        {'school_class': '11-1', 'scores': [5,3,2,5,5]}, #20 178 4
    ]

    avg_scores(school_classes)


if __name__ == "__main__":
    main()
