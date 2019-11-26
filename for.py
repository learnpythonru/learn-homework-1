"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    lst = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '4b', 'scores': [3,3,4,3,5]},
    {'school_class': '4c', 'scores': [4,4,5,4,4]},
    {'school_class': '4d', 'scores': [4,5,5,5,4]},]

    lst_total_grades = [i['scores'] for i in lst]
    total_students = sum([len(i) for i in lst_total_grades])
    
    school_average_grade = sum([sum(i) for i in lst_total_grades]) /total_students

    class_labels = [i['school_class'] for i in lst]
    class_grades = [sum(i)/len(i) for i in lst_total_grades]
    class_average_grade = list(zip(class_labels,class_grades))

    for i,j in class_average_grade:
        print( f'Average grade of class {i} is {j}')

    print(f"\nAverage grade across the whole school: {school_average_grade}")
    
if __name__ == "__main__":
    main()
