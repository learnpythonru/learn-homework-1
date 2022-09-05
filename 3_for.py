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

def get_total_sold(items_sold):
    summ = 0
    for item in items_sold:
        summ += item
    return summ

def get_average_sold(items_sold):
    summ = 0
    for item in items_sold:
        summ += item
    return summ / len(items_sold)

def total_sold_each_item(products):
    items_summ = []
    for product in products:
        item_summ_sold = get_total_sold(product['items_sold'])
        items_summ.append({product['product']: item_summ_sold})
    return items_summ

def total_sold_all_item(products):
    all_summ = 0
    for product in products:
        all_summ += get_total_sold(product['items_sold'])
    return all_summ

def average_sold_each_item(products):
    items_summ = []
    for product in products:
        item_summ_sold = get_average_sold(product['items_sold'])
        items_summ.append({product['product']: item_summ_sold})
    return items_summ

def average_sold_all_item(products):
    all_summ = 0
    for product in products:
        all_summ += get_average_sold(product['items_sold'])
    return all_summ


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(total_sold_each_item(phones))
    print(total_sold_all_item(phones))
    print(average_sold_each_item(phones))
    print(average_sold_all_item(phones))

if __name__ == "__main__":
    main()
