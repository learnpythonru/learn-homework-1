"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    journal = [
        {'school_class': '4-А', 'scores': [5, 5, 4]}, 
        {'school_class': '7-А', 'scores': [2, 3, 5, 2, 4]}, 
        {'school_class': '7-Б', 'scores': [3, 2, 2, 2, 2]}, 
        {'school_class': '8-А', 'scores': [4, 3, 4, 4, 3]}, 
        {'school_class': '9-А', 'scores': [5, 4, 4, 5, 5]}, 
    ]
    sum_school = 0
    count_school = 0
    for item in journal:
        sum_school += sum(item['scores'])
        count_school += len(item['scores'])
        avg = sum(item['scores']) / len(item['scores'])
        print(f'Средний балл {item["school_class"]} составляет {avg:.3}')
    print('=' * 10)
    avg_school = sum_school / count_school
    print(f'Средний балл по школе составляет {avg_school:.3}')

if __name__ == "__main__":
    main()
