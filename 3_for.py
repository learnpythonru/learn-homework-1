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

input_list = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def main():
    def calc_by_product():
        for product in input_list:
            items_sold = product["items_sold"]
            total_items = sum(items_sold)
            avg_items = total_items/len(items_sold)
            print(f"{product['product']}::: total items sold: {total_items}; on average: {int(round(avg_items,0))}")

    def all_products():
        final_list = []
        for product in input_list:
            final_list += product["items_sold"]
        total_all_products = sum(final_list)
        avg_all_products = total_all_products/len(final_list)
        print(f"Overall {total_all_products} items sold with {avg_all_products} on average.")

    calc_by_product()
    all_products()

if __name__ == "__main__":
    main()
