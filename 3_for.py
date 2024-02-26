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
    sales_data = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

    for product_data in sales_data:
        product = product_data['product']
        items_sold = product_data['items_sold']

        total_sales = sum(items_sold)
        average_sales = sum(items_sold) / len(items_sold)

        print(f"Товар: {product}")
        print(f"Общее количество продаж: {total_sales}")
        print(f"Среднее количество продаж: {average_sales}")
        print()

    all_items_sold = [item for product_data in sales_data for item in product_data['items_sold']]
    total_all_sales = sum(all_items_sold)
    average_all_sales = sum(all_items_sold) / len(all_items_sold)

    print("Общая информация по всем товарам:")
    print(f"Общее количество продаж всех товаров: {total_all_sales}")
    print(f"Среднее количество продаж всех товаров: {average_all_sales}")

if __name__ == "__main__":
    main()
