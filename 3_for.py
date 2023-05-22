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


def sum_sales_for_each_product(lsts):
    for lst in lsts:
        print(f'Cуммарное количество продаж товара: "{lst["product"]}" составляет {sum(lst["items_sold"])} шт.')


def avg_sales_for_each_product(lsts):
    for lst in lsts:
        print(f'Среднее количество продаж товара: "{lst["product"]}" составляет {round(np.average(lst["items_sold"]))} шт.')


def sum_sales_for_all_product(lsts):
    return f'Суммарное количество продаж товаров: "{", ".join([lst["product"] for lst in lsts])}" составляет {sum([sum(lst["items_sold"]) for lst in lsts])} шт.'


def avg_sales_for_all_product(lsts):
    return f'Среднее количество продаж товаров: "{", ".join([lst["product"] for lst in lsts])}" составляет {round(np.average([np.average(lst["items_sold"]) for lst in lsts]))} шт.'


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
    print(sum_sales_for_all_product(sales))
    print('_' * 75)
    print(avg_sales_for_all_product(sales))


if __name__ == "__main__":
    main()
