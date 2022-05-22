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
stock = [
  {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
  {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
  {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]

all_sum = 0
avg_sold = 0

def summ_each(each_phone):
    each_sum = 0
    for sell_each in each_phone:
        each_sum += sell_each
    return each_sum 
for one_phone in stock:
    one_sum = summ_each(one_phone['items_sold'])
    print(f"Cуммарное количество продаж {one_phone['product']}: {one_sum}")
    all_sum += one_sum

def avg_each(each_phone):
    each_sum = 0
    for sell_each in each_phone:
        each_sum += sell_each
    return each_sum / len(each_phone)
for one_phone in stock:
    one_sum = round(avg_each(one_phone['items_sold']), 2)
    print(f"Среднее количество продаж {one_phone['product']}: {one_sum}")
    avg_sold += one_sum

print(f"Cуммарное количество продаж всех телефонов: {all_sum}")
print(f"Среднее количество продаж всех телефонов: {avg_sold / len(str(all_sum))}")
