"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""



school = [
{'school_class': '4a', 'scores': [3,4,4,5,2]}, 
{'school_class': '4b', 'scores': [3,3,4,4,2]},
{'school_class': '4c', 'scores': [2,3,3,4,1]},
]

def main(school_avg, class_avg):
    school_avg_score = []
    for i in school_avg:
        for j in i.values():
            if type(j) == list:
                school_avg_score.append(sum(j) / len(j))
            else:
                continue 
    school_avg_score = sum(school_avg_score) / len(school_avg_score)   
    print(f'Средний балл по всей школе: {school_avg_score}')
    
    score_avg = 0
    class_name =''
    for i in school_avg:
        for j in i.values():

            if type(j) == list:
                score_avg += sum(j) / len(j)
                print(f'Средний балл класса {class_name} равен {score_avg}')
                score_avg = 0

            elif type(j) == str:
                class_name = j

if __name__ == "__main__":
    main(school, school)
