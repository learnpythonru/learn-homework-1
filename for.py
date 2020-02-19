"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
MARKS = [
    {"school_class": "7А", "scores": [4, 4, 4, 4, 3, 3, 5, 5, 5, 2]},
    {"school_class": "7Б", "scores": [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]},
    {"school_class": "8А", "scores": [3, 3, 3, 3, 4, 4, 4, 4, 5, 5]},
    {"school_class": "8Б", "scores": [2, 2, 4, 4, 5, 5, 5, 3, 3, 3]}
]


def avg(sequence):
    if len(sequence) > 0:
        return sum(sequence) / len(sequence)
    return 0


def average_for_class(class_name):
    for item in MARKS:
        if item["school_class"] == class_name:
            return avg(item["scores"])
        # класс отсутствует в списке
        return 0


def get_average_for_school():
    all_marks = [mark for class_info in MARKS for mark in class_info["scores"]]
    return avg(all_marks)


def main():
    avg_for_school = get_average_for_school()
    print(f"Средний балл школы - {avg_for_school}")
    for item in MARKS:
        class_name = item['school_class']
        avg_for_class = average_for_class(class_name)
        print(f"{class_name} - {avg_for_class}")


if __name__ == "__main__":
    main()
