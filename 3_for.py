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
#Создаём объект "all_phone_sold" со значениями из условия задания
all_phone_sold = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]

#Создаём функцию для вычисления среднего количества проданных телефонов
def sold_average(phone_items_sold):
    sold_sum = 0
    for item_sold in phone_items_sold:
        sold_sum += item_sold
    sold_avg = sold_sum/(len(phone_items_sold))
    return sold_avg
    
#Создаём функцию для вычисления суммарного количества проданных телефонов
def sold_phone(phone_items_sold):
    sold_sum = 0
    for item_sold in phone_items_sold:
        sold_sum += item_sold
    return sold_sum

for one_product in all_phone_sold:
    product_sold_phone = sold_phone(one_product['items_sold'])
    print(f"Суммарное количество продаж для телефона {one_product['product']}: {product_sold_phone}")

for one_product in all_phone_sold:
    product_sold_avg = sold_average(one_product['items_sold'])
    print(f"Среднее количество продаж для телефона {one_product['product']}: {product_sold_avg}")
   
avg_sold_sum = 0


print(f"Суммарное количество продаж: {product_sold_phone}")  
    
if __name__ == "__main__":
    main()
