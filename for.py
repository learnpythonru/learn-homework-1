"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
MARKS = [
  {"school_class": "7А", "scores": [4, 4, 4, 4, 3, 3, 5, 5, 5, 2]},
  {"school_class": "7Б", "scores": [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]},
  {"school_class": "8А", "scores": [3, 3, 3, 3, 4, 4, 4, 4, 5, 5]},
  {"school_class": "8Б", "scores": [2, 2, 4, 4, 5, 5, 5, 3, 3, 3]}
]

def avg(sequence):
  return sum(sequence)/len(sequence)

def average_for_class(class_name):
  for item in MARKS:
    if item["school_class"] == class_name:
      return avg(item["scores"])
  # класс отсутствует в списке
  return 0

def get_average_for_school():
  total = 0
  for item in MARKS:
    total += average_for_class(item["school_class"])
  count = len(MARKS)
  if count > 0:
    return total / count
  return 0


def main():
  print(f"Средний балл школы - {get_average_for_school()}")
  for item in MARKS:
    class_name = item['school_class']
    print(f"{class_name} - {average_for_class(class_name)}")
  

    
if __name__ == "__main__":
    main()
