"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
  s = 0
  l = 0
  d = [{'school_class': '4a', 'scores': [3,4,4,5,2]},\
      {'school_class': '5a', 'scores': [2,5,4,5]},\
      {'school_class': '5a', 'scores': [5,1,2,1,1]}]
  for i in d:
      s = s + sum(i['scores'])
      l = l + len(i['scores'])
      print('Cредний балл по классу', i['school_class'], ':', sum(i['scores'])/len(i['scores']))

  print('Cредний балл по всей школе: ', s/l)
    
if __name__ == "__main__":
    main()
