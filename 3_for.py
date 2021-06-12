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
    school = [
        {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
        {'school_class': '3b', 'scores': [4, 5, 5, 3, 4]},
        {'school_class': '5a', 'scores': [3, 3, 5, 2, 5]}
    ]

    scores_sum = 0
    scores_count = 0

    for s_class in school:
        for score in s_class['scores']:
            scores_sum += score
            scores_count += 1
    
    print('Средний балл по всей школе:', scores_sum / scores_count)

    for s_class in school:
        scores_sum = 0
        for score in s_class['scores']:
            scores_sum += score
        print(f'Средний балл {s_class["school_class"]}:', scores_sum / len(s_class['scores']))

    
if __name__ == "__main__":
    main()
