"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():

    school_info = [
        {'school_class': '4a', 'grades': [3, 3, 3, 3, 3]},
        {'school_class': '5b', 'grades': [4, 4, 4, 4, 4]},
        {'school_class': '6c', 'grades': [5, 5, 5, 5, 5]},
        {'school_class': '7z', 'grades': [2, 2, 2, 2, 2]},
    ]

    def count_avrg_school_grade(info):
        total_grade = 0
        amount_of_grades = 0

        for clas in info:
            total_grade += sum(clas['grades'])
            amount_of_grades += len(clas['grades'])

        average_grade = total_grade / amount_of_grades
        return f'Cредний школый балл: {average_grade}'

    def count_avrg_class_grade(info):
        class_grades = []

        for clas in info:
            average_grade = sum(clas['grades']) / len(clas['grades'])
            class_name = clas['school_class']
            class_grades.append(f'Средняя оценка класса {class_name}: {average_grade}')
        
        return '\n'.join(class_grades)

    print(count_avrg_school_grade(school_info))
    print(count_avrg_class_grade(school_info))

    
if __name__ == "__main__":
    main()
