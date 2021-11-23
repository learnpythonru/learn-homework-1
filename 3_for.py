"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
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
    average_scores.append(f'{value["school_class"]} = {average}')
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
