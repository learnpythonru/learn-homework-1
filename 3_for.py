"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""



class_marks = [
      {'school_class': '1a', 'scores': [3,4,4,5,2]},
      {'school_class': '1b', 'scores': [5,4,3,5,2]},
      {'school_class': '1c', 'scores': [3,5,2,2,2]},
      {'school_class': '1d', 'scores': [3,5,3,5,2]},
      {'school_class': '2a', 'scores': [5,4,2,5,2]},
      {'school_class': '2b', 'scores': [5,5,4,5,2]},
      {'school_class': '2c', 'scores': [2,4,5,5,2]},
      {'school_class': '2d', 'scores': [3,3,3,5,2]},
      {'school_class': '3a', 'scores': [3,4,5,3,5]},
      {'school_class': '3b', 'scores': [3,5,4,3,5]},
      {'school_class': '3c', 'scores': [3,2,2,5,2]},
      {'school_class': '3d', 'scores': [5,5,5,5,4]},
      {'school_class': '4a', 'scores': [5,4,4,5,3]},
      {'school_class': '4b', 'scores': [5,3,4,5,3]},
      {'school_class': '4c', 'scores': [5,4,4,4,4]},
      {'school_class': '4d', 'scores': [4,4,4,5,5]},
]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    avg_scores = []
    for cl in class_marks:
      cl_avg_score = sum(cl['scores'])/len(cl['scores'])
      print(f"Средний балл по классу {cl['school_class']} {cl_avg_score}")
      avg_scores.append(cl_avg_score)
    
    total_avg_score = sum(avg_scores)/len(avg_scores)
    print(f"Средний балл по всей школе {total_avg_score}")

  



    
if __name__ == "__main__":
    main()
