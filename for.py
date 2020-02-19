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


city_school = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]}, {'school_class': '4b', 'scores': [2, 5, 3, 4, 3]},
               {'school_class': '4c', 'scores': [4, 3, 2, 3, 4]}]

score_sum = 0
for score in city_school[0]['scores']:
    score_sum += score
    score_average_0 = score_sum / len(city_school[0]['scores'])

print(f'Средняя оценка 4а класса {score_average_0}')

for score in city_school[1]['scores']:
    score_sum += score
    score_average_1 = score_sum / len(city_school[1]['scores'])

print(f'Средняя оценка 4b класса {score_average_1}')

for score in city_school[2]['scores']:
    score_sum += score
    score_average_2 = score_sum / len(city_school[1]['scores'])

print(f'Средняя оценка 4c класса {score_average_2}')

general_score = score_sum

general_average = general_score / len(city_school)

print(f'Средняя оценка всей школы равна {general_average}')

if __name__ == "__main__":
    main()
