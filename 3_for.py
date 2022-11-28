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
from itertools import count, product


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    phone = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

    for i in range(len(phone)):
      name = phone[i]['product']
      summ = 0
      for sale_one_model in phone [i] ['items_sold']:
        summ = summ + sale_one_model
      avg_score_model = summ / len(phone[i]['items_sold'])
      print(f'суммарное количество продаж для {name}: {summ}')
      print(f'среднее количество продаж для {name}: {avg_score_model}')

    full_list = []
    for i in range(len(phone)):
      lists = phone[i]['items_sold']
      for y in lists:
        full_list.append(y)
    print("суммарное количество продаж всех товаров:", sum(full_list))
    print('среднее количество продаж всех товаров:', sum(full_list) / len(full_list))

    

    

      
    
if __name__ == "__main__":
    main()