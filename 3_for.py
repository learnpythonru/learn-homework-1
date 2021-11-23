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
