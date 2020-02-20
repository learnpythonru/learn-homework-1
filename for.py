"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
grades = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
          {'school_class': '4b', 'scores': [5,5,4,2,2]},
          {'school_class': '4c', 'scores': [4,4,5,5,5]}]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    scores_sum = 0
    for x in grades:
        x['average_score'] = sum(x['scores'])/len(x['scores'])
        print('Class ', x['school_class'],': ',x['average_score'])
        scores_sum += x['average_score']
    print("Total average score: ", scores_sum/len(grades))
if __name__ == "__main__":
    main()
