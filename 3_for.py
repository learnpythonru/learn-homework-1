"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    dict_ = [
        {
            'school_class': '4a', 
            'scores':[3,4,4,5,2]
        },
        {   'school_class': '4b',
            'scores':[4,4,4,3,3]
        },
        {
            'school_class': '4c',
            'scores':[2,2,3,4,5]
        }
    ]
    
    scores_sum = 0
    for i in dict_:
        scores_sum += sum(i['scores']) / len(i['scores'])
    all_score = scores_sum/len(dict_)
    print(f'AVG po shkole: {all_score}')
    
    for i in dict_:
        print(f'AVG po classu "{i["school_class"]}":' 
        f' {sum(i["scores"]) / len(i["scores"])}')
        

main()

