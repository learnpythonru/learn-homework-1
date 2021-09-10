"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
from rich import print

scores1 = [
  {'school_class': '1a', 
   'scores': [
    5,4,2,2,5
  ]},
  {'school_class': '2a', 
   'scores': [
    4,5,3,2,5
  ]},
  {'school_class': '3a', 
   'scores': [
    3,5,3,2,5
  ]},
  {'school_class': '4a', 
   'scores': [
    5,5,4,3,5
  ]},
  {'school_class': '5a', 
   'scores': [
    2,2,3,4,5
  ]},
]

# scores1 = [
#   {'school_class': '1a', 
#    'scores': [
#     5,4,5,4
#   ]},
#   {'school_class': '2a', 
#    'scores': [
#     5,5,5,5,5
#   ]}
# ]
    
def get_avg_class_score(groups):
  avg_scores = {}
  for group in groups:
    name = group['school_class'] 
    scores = group['scores']
    avg_scores[name] = sum(scores) / len(scores)
    
  return avg_scores
     
def get_avg_school_score(groups): 
  total_score = 0
  total_count = 0
  
  for group in groups:
    scores = group['scores']
    total_score += sum(scores)
    total_count += len(scores)
  
  return total_score / total_count

def main():
    print(get_avg_class_score(scores1))
    print(get_avg_school_score(scores1))
    
if __name__ == "__main__":
    main()
