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
    lst_scores = [
      {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '4b', 'scores': [3,5,4,3,2]}, 
    {'school_class': '4c', 'scores': [5,3,4,2,2]},
    {'school_class': '4d', 'scores': [4,4,4,4,4]}
    ]
    
    for school_class in lst_scores:
      scores_sum = 0
      for score in school_class['scores']:
        scores_sum += score
      current_class = school_class['school_class']
      avg_score = scores_sum/len(school_class['scores'])
      print('Средний балл в', current_class, ':', avg_score)
  
      school_class['class_avg_score'] = avg_score

    scores_sum = 0
    for school_class in lst_scores:
      scores_sum += school_class['class_avg_score']
    school_avg_score = scores_sum/len(lst_scores)
    print()
    print('Средний балл по всей школе :', school_avg_score)


    
    
if __name__ == "__main__":
    main()
