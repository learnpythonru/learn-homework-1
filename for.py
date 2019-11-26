"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
school_journal = [
                {'school_class': '4a', 'scores': [3,5,4,5,4]},
                {'school_class': '4b', 'scores': [3,4,5,5,3]},
                {'school_class': '4c', 'scores': [5,4,5,5,5]},
                {'school_class': '5b', 'scores': [2,4,3,2,2]},
                {'school_class': '5a', 'scores': [3,4,3,5,3]},
                {'school_class': '6a', 'scores': [5,4,4,5,5]}
]

def main():

    sum_school_score = 0
    caunt_score = 0

    for score in school_journal:
        sum_school_score += sum(score["scores"])
        caunt_score += len(score["scores"])

        secondary_schools = sum_school_score / caunt_score

        secondary_class = sum(score['scores']) / len(score['scores'])

        number_class = score['school_class']

        print(f'Средний бал в классе {number_class} : {secondary_class}')
    
    print(f'Среднее бал по школе: {secondary_schools}')

    
if __name__ == "__main__":
    main()








