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
phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def main():
 for product in phones:
    product_name = product['product']  # внесены переменные для удобства чтения кода
    sales = product['items_sold']
    total_sales = sum(sales)
    avg_sales = total_sales / len(sales)
    print(f"Продукт: {product_name}, кол-во продаж: общие - {total_sales}, средние - {avg_sales:.0f}")

count_all_sales = sum([sum(sales['items_sold']) for sales in phones])
avg_all_sales = count_all_sales / len(phones)
print(f"Cуммарное количество продаж всех товаров: {count_all_sales}")
print(f"Cреднее количество продаж всех товаров: {avg_all_sales:.0f}")
    
if __name__ == "__main__":
    main()

    
    