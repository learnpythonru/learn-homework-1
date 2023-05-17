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

sales_info = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    total_sales = 0
    total_sale_times = 0

    print('1-2. Суммарное/среднее количество продаж по товарам:')
    for product in sales_info:
        total_product_sales = sum(product["items_sold"])
        total_product_sale_times = len(product["items_sold"])
        avg_product_sales = round(total_product_sales/total_product_sale_times)

        total_sales += total_product_sales
        total_sale_times += total_product_sale_times

        print(f'\t{product["product"]} - {total_product_sales}/{avg_product_sales}')

    print(f'\n3. Cуммарное количество продаж всех товаров: {total_sales}')

    print(f'\n4. Cреднее количество продаж всех товаров: {round(total_sales/total_sale_times)}')


if __name__ == "__main__":
    main()
