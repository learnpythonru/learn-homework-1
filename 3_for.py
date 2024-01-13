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

from pprint import pprint
from statistics import mean

sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]

def main():
    for count_sales in sales:
        sales_sum = sum(count_sales.get('items_sold'))
        average_value = mean(count_sales.get('items_sold'))
        total_sales_sum = sum(int(str.join(count_sales['items_sold'])))
        print(f'Суммарное количество продаж {count_sales.get('product')}: ', sales_sum)
        print(f'Среднее количество продаж {count_sales.get('product')}: ', average_value)
        print(total_sales_sum)
        

if __name__ == "__main__":
    main()

classes = [
    {'name': '3А', 'scores': [3,4,4,5,2]},
    {'name': '3Б', 'scores': [5,5,3,2,2]},
    {'name': '3В', 'scores': [4,5,3,5,4]},
]

def count_average(students_scores):
    scores_sum = 0
    for score in students_scores:
        scores_sum += score
    scores_avg = scores_sum / len(students_scores)
    return scores_avg

for one_class in classes:
    class_score_avg = count_average(one_class['scores'])
    print(f"Средняя оценка для класса {one_class['name']}: {class_score_avg}")