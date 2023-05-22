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

sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]


def product_sales(product):
    return sum(product["items_sold"])


def product_sale_times(product):
    return len(product["items_sold"])


def total_sales(sales_dict):
    return sum([product_sales(product) for product in sales_dict])


def total_sale_times(sales_dict):
    total_sales_times = sum([product_sale_times(product) for product in sales_dict])
    return total_sales_times


def avg_sale(sales, sale_times):
    return round(sales/sale_times)


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    print('1. Суммарное количество продаж по товарам:')
    for product in sales:
        print(f'\t{product["product"]}: {product_sales(product)}')

    print('\n2. Среднее количество продаж по товарам:')
    for product in sales:
        print(f'\t{product["product"]}: {avg_sale(product_sales(product), product_sale_times(product))}')

    print(f'\n3. Cуммарное количество продаж всех товаров: {total_sales(sales)}')

    print(f'\n4. Cреднее количество продаж всех товаров: '
          f'{avg_sale(total_sales(sales), total_sale_times(sales))}')


if __name__ == "__main__":
    main()
