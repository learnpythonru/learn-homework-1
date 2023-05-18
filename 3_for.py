import numpy as np

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


def sum_sales_for_each_product(lst):
    for i in lst:
        print(f'Cуммарное количество продаж товара: "{i["product"]}" составляет {sum(i["items_sold"])} шт.')


def avg_sales_for_each_product(lst):
    for i in lst:
        print(f'Среднее количество продаж товара: "{i["product"]}" составляет '
              f'{round(np.average(i["items_sold"]))} шт.')


def sum_sales_for_all_product(lst):
    print(f'Суммарное количество продаж товаров: "{", ".join([i["product"] for i in lst])}" составляет '
          f'{sum([sum(i["items_sold"]) for i in lst])} шт.')


def avg_sales_for_all_product(lst):
    print(f'Среднее количество продаж товаров: "{", ".join([i["product"] for i in lst])}" составляет '
          f'{round(np.average([np.average(i["items_sold"]) for i in lst]))} шт.')


def main():
    sales = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    sum_sales_for_each_product(sales)
    print('_' * 75)
    avg_sales_for_each_product(sales)
    print('_' * 75)
    sum_sales_for_all_product(sales)
    print('_' * 75)
    avg_sales_for_all_product(sales)


if __name__ == "__main__":
    main()
