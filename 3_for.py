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
    school_classes = [
                        {'school_class': '4a', 'scores': [3, 4, 4, 5, 1]},
                        {'school_class': '7b', 'scores': [4, 4, 5, 5, 3]},
                        {'school_class': '2c', 'scores': [5, 3, 1, 5, 4]}
                    ]

    school_mean_score = []
    for school_class in school_classes:
        school_mean_score.extend(school_class['scores'])
        print('Class {} mean score = {}'.format(school_class['school_class'], sum(school_class['scores']) / len(school_class['scores'])))

    print('School mean score = {}'.format(sum(school_mean_score) / len(school_mean_score)))

    #pass
    
if __name__ == "__main__":
    main()
