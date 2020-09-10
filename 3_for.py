"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school = [
            {'school_class': '4a', 'scores': [5,4,2,5,2]}, 
            {'school_class': '5a', 'scores': [3,4,4,5,4]}, 
            {'school_class': '6a', 'scores': [2,4,4,5,3,5,3,4]}, 
            {'school_class': '7a', 'scores': [4,4,2,5,3]}, 
            {'school_class': '8a', 'scores': [4,5,2,5,3]},
            {'school_class': '9a', 'scores': [4,4,2,5,3]}
    ]
    
    school_sum = 0
    class_sum = 0

    for grade in school:
       
        for score in grade['scores']:
            class_sum += score
        
        class_avg = class_sum / len(grade['scores'])
        print(f"Средняя оценка класса {grade['school_class']}: {class_avg}")
        
        class_sum = 0
        school_sum += class_avg
    
    school_avg = school_sum / len(school)
    print(f"\nСредняя оценка в школе: {school_avg}")

if __name__ == "__main__":
    main()
