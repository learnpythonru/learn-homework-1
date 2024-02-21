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

product_list = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]


def count_sold_items(items_sold: list) -> int:
    count_items = 0
    for item in items_sold:
        count_items += item
    return count_items


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    for product in product_list:
        count_sold_products = count_sold_items(product['items_sold'])
        print(f" Модель {product['product']} продано: {count_sold_products}")
    print()

    all_count_sold_items = 0
    for product in product_list:
        count_sold_products = count_sold_items(product['items_sold'])
        all_count_sold_items += count_sold_products
        print(
            f" Модель {product['product']} среднее кол-во продаж: "
            f"{round(count_sold_products / len(product['items_sold']))}"
        )

    for product in product_list:
        count_sold_products = count_sold_items(product['items_sold'])
        all_count_sold_items += count_sold_products
    print()
    print(f"Общее количество проданных товаров: {all_count_sold_items}")
    print(f"Среднее кол-во продаж всех товаров: {round(all_count_sold_items / len(product_list))}")


if __name__ == "__main__":
    main()
