"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
groups = [{'school_class' : '4A', 'scores' : [5,3,4,5,5]},
    {'school_class' : '4B', 'scores' : [4,2,1,2,5]},
    {'school_class' : '4C', 'scores' : [4,5,5,2,2]}]

def class_score():
    total_score = 0
    total_students = 0
    for group in groups: # для каждой группы в группах
        name = group['school_class']
        scores = group['scores']
        average_group_rating = (sum(scores))/(len(scores))
        print(f'Средний бал класса {name}: {average_group_rating}')
        total_score += sum(scores)
        total_students += len(scores)

    average_school_rating = total_score/total_students
    print(f'Средний бал всей школы {average_school_rating}')

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    class_score()

if __name__ == "__main__":
    main()
