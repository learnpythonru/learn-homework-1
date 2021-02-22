"""
Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_classroom': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
# Задаём список из словарей в который будем передавать оценки учеников
classroom_scores = [
    {'classroom': '4a', 'scores': []},
    {'classroom': '4b', 'scores': []},
    {'classroom': '4c', 'scores': []},
    {'classroom': '4d', 'scores': []}
]

# В цикле считываем оценки учеников для каждого класса (класса школы :))
for item in classroom_scores:
    classroom = item['classroom']  
    item['scores'] = input(f'Введите через пробел оценки учеников класса {classroom} ').split()
    item['scores'] = [int(elem) for elem in item['scores']]

"""Calculate and displays the average score from school and classroomes"""
def main(classroom_scores):
    sum_scores = 0                                           
    sum_avg_scores = 0
    for item in classroom_scores:
        sum_scores += sum(item['scores'])
        avg_scores = sum_scores / len(item['scores'])
        sum_avg_scores += avg_scores
        
        classroom = item['classroom']
        print(f'Cредний балл по классу {classroom}: {avg_scores}')
        sum_scores = 0
    
    avg_school_scores = sum_avg_scores / len(classroom_scores)
    print(f'Cредний балл по параллели: {avg_school_scores}')
    return avg_school_scores

if __name__ == "__main__":
    main(classroom_scores)