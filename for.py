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
    school = [{'school_class': '4a', 'scores': [3,4,4,5,2,3,5,4,2]}, 
    {'school_class': '1б', 'scores': [2,4]},
    {'school_class': '11в', 'scores': [5,5,4,4,3,5,4]},
    {'school_class': '6a', 'scores': [4,4,5,3]},
    {'school_class': '6г', 'scores': [4,5,2,5,4,3]},
    {'school_class': '9д', 'scores': [4,4,5,3,4,5,5,5,5,5,5,5,5,5]},
    {'school_class': '8б', 'scores': [3,4,4,4,3,5]},
    {'school_class': '7ж', 'scores': [4,4,3,4,4,2,4,2]}]

    result2 = []
    for score in school:
        result1 = "Average grade in classes: " + score["school_class"] + " " +\
                  str(round(sum(score["scores"])/len(score["scores"]),2))
        result2.append(sum(score["scores"])/len(score["scores"]))
        print(result1)
    avarage_school_score = "Average school grade for all classes: " + str(round(sum(result2)/len(result2),2))
    print(avarage_school_score)



    
if __name__ == "__main__":
    main()

