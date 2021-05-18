"""

Домашнее задание №3

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

school_metr = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '5b', 'scores': [5,4,4,5,3,4,3,5]},
    {'school_class': '7d', 'scores': [3,3,2,5,2,2,2,5,5,5,3]},]

def main():
    school_score = 0
    overall_mark_count = 0

    for i in school_metr:
        class_score = 0
        for s in i["scores"]:
            class_score += s
            overall_mark_count += 1
        print(f'Средний балл по {i["school_class"]} : {round((class_score / len(i["scores"])), 2)}')
        school_score += class_score

    print(f'Средний балл по школе: {round((school_score / overall_mark_count), 2)}')

if __name__ == "__main__":
    main()
