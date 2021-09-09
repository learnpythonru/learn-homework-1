"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

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
     
# this is the custom class for pushing things in list
class List(list):
    def push(self, x):
        self.append(x)

averageClassScores = List()

def defineAverageScoreWithinClass(scores, averageClassScores = List()):
  for each in scores:
    averageClassScores.push((sum(each['scores']) / len(each['scores'])))
    
    # print(each['school_class'])
    # print(each['scores'])
    
    # it does not work - why?
    # return (f"The average score of class: {each('school_class')} is { sum(each('scores')) / len(each('scores'))}")
  
  print(f'The average class scores are { averageClassScores }')
  return(averageClassScores)
     
def defineAverageScoreWithinSchool(scores):
  scores = (defineAverageScoreWithinClass(scores1))
  return(f'The average score within school is: {sum(scores) / len(scores)}')

def main():
    print(defineAverageScoreWithinSchool(scores1))
    
if __name__ == "__main__":
    main()
