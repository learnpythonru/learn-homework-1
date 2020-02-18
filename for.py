import random

"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    classes_literal = ['а','б','в','г','д']
    classes_number = [str(x) for x in range(1, 12)]
    school = []
    total_score = []
    for x in range(10):
      class_name = random.choice(classes_number) + random.choice(classes_literal)
      school.append({'school_class': class_name, 'scores': [random.randint(2, 5) for x in range(10)]})
    
    for school_class in school:
        print('{:<3} = {}'.format(school_class['school_class'], sum(school_class['scores']) / len(school_class['scores'])))
        total_score.extend(school_class['scores'])

    avg_school_score = sum(total_score) / len(total_score)
    print('Средний балл по всей школе: {}'.format(avg_school_score))


if __name__ == "__main__":
    main()
