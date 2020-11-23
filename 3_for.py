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
    school_classes_rate = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
                           {'school_class': '4b', 'scores': [2, 5, 4, 5, 2]},
                           {'school_class': '4c', 'scores': [2, 3, 3, 3, 2]}]

    def average_of_class(some_list):
        avg = sum(some_list) / len(some_list)
        return avg

    def average_of_classes(some_dict):
        sum_scores = 0
        len_sum_scores = 0
        for i in range(len(some_dict)):
            len_scores = len(some_dict[i]['scores'])
            n = sum(some_dict[i]['scores'])
            len_sum_scores += len_scores
            sum_scores += n
        return round(sum_scores / len_sum_scores, 2)

    for i in range(len(school_classes_rate)):
        print(f"Средний балл у {school_classes_rate[i]['school_class']}: {average_of_class(school_classes_rate[i]['scores'])}")

    print(f'Среднее по всей школе: {average_of_classes(school_classes_rate)}')


if __name__ == "__main__":
    main()
