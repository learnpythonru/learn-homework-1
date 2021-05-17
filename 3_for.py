"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
scool_list = [{'school_class': '1a', 'scores': [5,4,4,5,4]}, 
              {'school_class': '2a', 'scores': [5,4,5,5,5]},
              {'school_class': '3a', 'scores': [3,4,4,3,2]},
              {'school_class': '4a', 'scores': [3,4,2,5,2]}]

def arithmrtic_mean(lst: list) -> int :  # функция вычисляет среднее арифметическое и округляет результат
    result = int(sum(lst)/len(lst))
    return result

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    global scool_list
    mid_school_score = []

    for scores in scool_list:
        mid_score_in_class = arithmrtic_mean(scores.get("scores"))
        mid_school_score.append(mid_score_in_class)
        print(f'{scores.get("school_class")} - средняя оценка в классе: {mid_score_in_class}')

    print(f'Средняя оценка в школе: {arithmrtic_mean(mid_school_score)}')

    
if __name__ == "__main__":
    main()
