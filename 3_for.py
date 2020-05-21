"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

dict_grades = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '5a', 'scores': [5, 5, 3, 4]},
    {'school_class': '6a', 'scores': [4, 3, 4, 5, 3, 5, 5]},
    {'school_class': '7a', 'scores': [4, 5, 5, 2, 3, 4]},
    {'school_class': '8a', 'scores': [4, 5, 4, 3, 4]},
]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """


# Средний балл по школе
summ = 0
for grade in dict_grades:
    summ += sum(grade['scores']) / len(grade['scores'])

print(round(summ / len(dict_grades), 2))

# Средний балл по каждому классу
for grade in dict_grades:
    print('{}: {}'.format(grade['school_class'], round(sum(grade['scores']) / len(grade['scores']), 2)))

if __name__ == "__main__":
    main()
