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
    return [sum(lst["items_sold"]) for lst in lsts]


def avg_sales_for_each_product(lsts):
    return [round(sum(lst["items_sold"])/len(lst["items_sold"])) for lst in lsts]


def sum_sales_for_all_products(lsts):
    return sum(sum_sales_for_each_product(lsts))


def avg_sales_for_all_products(lsts):
    return round(sum_sales_for_all_product(lsts) / len(lsts))

def main():
    sales = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    for i in range(len(sales)):
        print(f'Cуммарное количество продаж товара: "{sales[i]["product"]}" составляет {sum_sales_for_each_product(sales)[i]} шт.')
    print('_' * 75)

    for i in range(len(sales)):
        print(f'Среднее количество продаж товара: "{sales[i]["product"]}" составляет {avg_sales_for_each_product(sales)[i]} шт.')
    print('_' * 75)

    print(f'Суммарное количество продаж товаров: "{", ".join([sale["product"] for sale in sales])}" составляет {sum_sales_for_all_products(sales)} шт.')
    print('_' * 75)

    print(f'Среднее количество продаж товаров: "{", ".join([sale["product"] for sale in sales])}" составляет {avg_sales_for_all_products(sales)} шт.')


if __name__ == "__main__":
    main()
