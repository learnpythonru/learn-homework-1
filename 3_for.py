"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

# scores1 = [
#   {'school_class': '1a', 
#    'scores': [
#     5,4,2,2,5
#   ]},
#   {'school_class': '2a', 
#    'scores': [
#     4,5,3,2,5
#   ]},
#   {'school_class': '3a', 
#    'scores': [
#     3,5,3,2,5
#   ]},
#   {'school_class': '4a', 
#    'scores': [
#     5,5,4,3,5
#   ]},
#   {'school_class': '5a', 
#    'scores': [
#     2,2,3,4,5
#   ]},
# ]

# the average value is 5 there - for check
# scores1 = [
#   {'school_class': '1a', 
#    'scores': [
#     5,5
#   ]},
#   {'school_class': '2a', 
#    'scores': [
#     5,5
#    ]},
#   {'school_class': '3a', 
#    'scores': [
#     5,5
#    ]},
#   {'school_class': '4a', 
#    'scores': [
#     5,5
#    ]},
#   {'school_class': '5a', 
#    'scores': [
#     5,5
#    ]},
# ]


scores1 = [
  {'school_class': '1a', 
   'scores': [
    5,4,5,4
  ]},
  {'school_class': '2a', 
   'scores': [
    5,5,5,5,5
  ]}
]
    
# this is the custom class for pushing things in list
class List(list):
    def push(self, x):
        self.append(x)

avg_class_scores = List()

def get_avg_class_score(scores, avg_class_scores = None):
  # пчм мы не можем создать массив для хранения средних оценок внутри функции?
  avg_class_scores = List()

  for score in scores:
    avg_class_scores.push((sum(score['scores']) / len(score['scores'])))
    
    # changed brakets but still don'r work
    # return (f"The average score of class: {score['school_class']} is { sum(score['scores']) / len(score['scores'])}")
  
  print(f'The average class scores are { avg_class_scores }')
  return(avg_class_scores)
     
# def get_avg_school_score(scores):
  # why cannot we get avg of average class scores?
  
  # scores = (get_avg_class_score(scores1))
  # print(scores)
  # print(sum(scores))
  # print(len(scores))
  # return(f'The average score within school is: {sum(scores) / len(scores)}')

def main():
    print(get_avg_school_score(scores1))
    
# if __name__ == "__main__":
#     main()
