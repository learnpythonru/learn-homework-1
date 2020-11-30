"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

scores =  [
  {
    'school_class': '4a', 
    'scores': [3,4,4,5,2,3,5,4,5,5,4,3,5]
  },
  {
    'school_class': '5b', 
    'scores': [5,4,5,3,3,4,2,4,5,4,3,5,4]
  },
  {
    'school_class': '7a', 
    'scores': [4,4,4,5,3,3,4,5,4,3,2,5,4]
  }
]

def main(school_scores):
  classes_scores = []
  for clas in school_scores:
    clas_avg_score = get_avg_scores(clas['scores'])
    print(f'Средняя оценка класса {clas["school_class"]} равна {clas_avg_score}')
    classes_scores.append(clas_avg_score)
  print('Средняя оценка школы ' + str(get_avg_scores(classes_scores)))


def get_avg_scores(school_scores):
    scores_sum = 0
    for score in school_scores:
        scores_sum += score

    scores_avg = scores_sum / len(school_scores)
    return scores_avg


if __name__ == "__main__":
    main(scores)
