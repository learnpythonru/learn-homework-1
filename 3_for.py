#!/usr/bin/python3.8
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

salesdict = [
    {
        'product': 'iPhone 12',
        'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]
    },
    {
        'product': 'Xiaomi Mi11',
        'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]
    },
    {
        'product': 'Samsung Galaxy 21',
        'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]
    },
]


def main():
    total_sales = 0
    avg_sales = 0
    for sales in range(len(salesdict)): 
        ssum = 0
        for sale in range(len(salesdict[sales]["items_sold"])):
            ssum += salesdict[sales]["items_sold"][sale]
        print(f'Суммарное количество продаж для товара {salesdict[sales]["product"]} = {ssum}') 
        print(f'Среднее количество продаж для товара {salesdict[sales]["product"]} = {ssum / len(salesdict[sales]["items_sold"])}') 
        total_sales += ssum
        avg_sales += ssum / len(salesdict[sales]["items_sold"])

    print(f'Cуммарное количество продаж всех товаров {total_sales}')
    print(f'Cреднее количество продаж всех товаров {total_sales / len(salesdict)}')

if __name__ == "__main__":
    main()
