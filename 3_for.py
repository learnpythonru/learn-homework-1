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


def sales_counting():
    sold_phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
    
    sum_sold = 0
    avarege_sold = 0
    for dict_ in sold_phones:
        sum_product_sold = 0
        avarege_product_sold = 0
        sum_product_sold = sum(dict_['items_sold'])
        sum_sold += sum_product_sold
        avarege_product_sold = sum(dict_['items_sold']) / len(dict_['items_sold'])
        avarege_sold += avarege_product_sold
        print (f"Cуммарное количество продаж для {dict_['product']}: {sum_product_sold}") 
        print (f"Cреднее количество продаж для {dict_['product']}: {avarege_sold}")
    print (f"Cуммарное количество продаж всех товаров: {sum_sold}") 
    print (f"Cреднее количество продаж всех товаров: {avarege_sold / len(sold_phones)}")


def main():
    sales_counting()


if __name__ == "__main__":
    main()
