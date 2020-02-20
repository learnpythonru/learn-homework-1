"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
from random import randint, choice


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school = {}
    school_literal = ['a', 'b']
    rating_list = [{'school_class': str(randint(1, 12)) + choice(school_literal),
                    'scores': [randint(1, 5) for x in range(12)]} for x in range(20)]

    # вычислим средний бал по каждому классу и добавим его в словарь
    for dicts in rating_list:
        class_sum = 0
        for items in dicts['scores']:
            class_sum += items
        class_avg = class_sum / len(dicts['scores'])
        school[dicts['school_class']] = class_avg

    # вычислим средний бал по всей школе
    school_sum = 0
    for value in school.values():
        school_sum += value
    school_avg = school_sum / len(school)

    # Вывод информации
    print('Средний бал по всей школе: {:.2f}'.format(school_avg))
    for key, value in school.items():
        print('Средний бал по {} классу: {:.2f}'.format(key, value))


if __name__ == "__main__":
    main()
