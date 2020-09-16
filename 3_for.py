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
    list_students = [
        {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
        {'school_class': '5a', 'scores': [3, 1, 4, 5, 2]},
        {'school_class': '6a', 'scores': [3, 4, 4, 2, 5]},
        {'school_class': '7a', 'scores': [1, 4, 4, 5, 2]},
        {'school_class': '8a', 'scores': [3, 4, 1, 3, 2]},
        {'school_class': '9a', 'scores': [3, 1, 4, 5, 1]},
        {'school_class': '10a', 'scores': [3, 3, 3, 5, 2]},
    ]


    sum_mark = 0
    count_mark = 0
    for class_students in list_students:
        sum_class = 0
        for n in class_students['scores']:
            sum_mark += n
            count_mark += 1
            sum_class += n
        print(f"school_class: {class_students['school_class']} "
              f"avg: {sum_class / len(class_students['scores'])}")

    print(f"avg all school: {sum_mark / count_mark}")


if __name__ == "__main__":
    main()
