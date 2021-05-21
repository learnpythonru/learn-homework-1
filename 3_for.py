"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
school_data = [
    {"school_class": "4a", "scores": [3, 4, 4, 5, 2]},
    {"school_class": "4b", "scores": [3, 5, 5, 5, 5]},
    {"school_class": "5", "scores": [3, 3, 4, 3, 2]},
    {"school_class": "5b", "scores": [3, 3, 3, 3, 3]},
]

def school_estim(data_dict):
    class_nb = len(school_data) # number of classes in school
    score_school_m = 0    

    for school_c in data_dict:
        score_m = sum(school_c["scores"])/len((school_c["scores"]))
        score_school_m += score_m
        print(f"Average score in {school_c['school_class']} is {score_m}")
    print('Average score in school is', score_school_m/class_nb )
    
if __name__ == "__main__":
    school_estim(school_data)
