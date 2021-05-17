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

def main():
    score_avg = 0
  
    for i in school:
        score_avg += sum(school[i]['scores']) / len(school[i]['scores'])
    print(score_avg)


    
if __name__ == "__main__":
    main()
