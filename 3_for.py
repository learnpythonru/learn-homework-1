"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
  school = [{'school_class': '2a', 'scores':[5, 5, 4, 4, 3, 2, 5]},
	        {'school_class': '11b', 'scores':[5, 3, 2, 5, 3, 2, 5]},
	        {'school_class': '9a', 'scores':[5, 5, 5, 5, 2, 5, 5]}]
  scores_class = 0
  scores_school = 0
  i = 0
  for classes in school:      
    for  score in classes['scores']:      
      scores_class += score
    print(scores_class/len(classes['scores'])) 
    scores_school += scores_class/len(classes['scores'])
    scores_class = 0
    i += 1  
  print(scores_school/len(school))


if __name__ == "__main__":
    main()
