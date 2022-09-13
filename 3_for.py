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
from distutils.command.install_egg_info import safe_name


user_dict = [
{'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
{'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
{'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]
 
def first_func(sum_sold_one_model):
    sum_model_phone = 0
    for item in sum_sold_one_model:
        sum_model_phone += item
    return sum_model_phone
print(f'Total sold iphone 12:',first_func(user_dict[0]['items_sold']))
print(f'Total sold Xiaomi Mi11:',first_func(user_dict[1]['items_sold']))
print(f'Total sold Samsung Galaxy 21:',first_func(user_dict[2]['items_sold']))


def second_func(avg_sold_one_model):
    sum_model_phone = 0
    for item in avg_sold_one_model:
        sum_model_phone += item
    avg_sum = round(sum_model_phone / len(avg_sold_one_model), 3)
    return avg_sum
print(f'Average sold iphone 12:',second_func(user_dict[0]['items_sold']))
print(f'Average sold Xiaomi Mi11:',second_func(user_dict[1]['items_sold']))
print(f'Average sold Samsung Galaxy 21:',second_func(user_dict[2]['items_sold']))


def third_func(total_sold_all_models):
    sum_sold_one_model = 0
    for item in total_sold_all_models:
        sum_sold_one_model += item
    return sum_sold_one_model
total_sum_all_models = 0
for item in user_dict:
    total_sum_all_models += third_func(item['items_sold'])
print(f'Total sold all phones: {total_sum_all_models}')