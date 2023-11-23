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


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    data = [
        {
            "product": "iPhone 12",
            "items_sold": [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186],
        },
        {
            "product": "Xiaomi Mi11",
            "items_sold": [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316],
        },
        {
            "product": "Samsung Galaxy 21",
            "items_sold": [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247],
        },
    ]
    data_by_product = {
        "sum": {},
        "average": {},
    }
    sum_count_sales_all_products = 0
    for sales in data:
        data_by_product["sum"][sales["product"]] = sum(sales["items_sold"])
        data_by_product["average"][sales["product"]] = data_by_product["sum"][
            sales["product"]
        ] / len(sales["items_sold"])
        sum_count_sales_all_products += data_by_product["sum"][sales["product"]]

    average_count_sales_all_products = sum_count_sales_all_products / len(
        data_by_product["sum"]
    )

    print(f'Суммарное количество продаж для каждого товара:\n{data_by_product["sum"]}')
    print(
        f'Среднее количество продаж для каждого товара:\n{data_by_product["average"]}'
    )
    print(
        f"Суммарное количество продаж для всех товаров: {sum_count_sales_all_products}"
    )
    print(
        f"Среднее количество продаж для всех товаров: {average_count_sales_all_products}"
    )


if __name__ == "__main__":
    main()
