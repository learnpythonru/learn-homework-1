"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
raiting = [{'school_class': '4a', 
          'scores': [3,4,4,5,2]}, 
          {'school_class': '5a', 
          'scores': [2,4,2,3,4]},
          {'school_class': '6a', 
          'scores': [5,2,4,3,2]},
          ]
def get_average_class_raiting():
  average_scores = []
  for value in raiting:
    average = value["average_score"] = sum(value["scores"]) / len(value["scores"])  # добавляем в словарь среднюю оценку
    average_scores.append(f'{value["school_class"]} = {str(average)}')
  return average_scores
    

def get_average_school_raiting():
  average_scores = []   # заморочиться и попробовать создать список одним списочным выражением
  for score in raiting:
      average_scores.extend(score['scores'])      # идем по словарю, находим оценки и добавляем их в список.
  return round(sum(average_scores) / len(average_scores), 2)

def main():
    print("Средний балл по школе", get_average_school_raiting())
    print("Средний балл по каждому классу", *get_average_class_raiting())
if __name__ == "__main__":
    main()
