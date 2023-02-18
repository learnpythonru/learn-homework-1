"""

Домашнее задание №1

Цикл for: Продажи товаров

* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

phone_sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


def count_sum_sale(item_sold):
    """Считаю сумму всех покупок одного товара"""
    sum = 0
    for sold in item_sold:
        sum += sold
    return sum


def print_sum_sale_per_phone(phone_sales):
    """Вывожу сумму всех покупок для каждого товара"""
    total_sum_sale = 0

    for sales in phone_sales:
        sum_sale = count_sum_sale(sales['items_sold'])
        print(f'Суммарное количество продаж {sales["product"]} : {sum_sale}')
        # Сумма продаж всех товаров
        total_sum_sale += sum_sale
    print(f'Сумма продаж всех товаров: {total_sum_sale}')


def count_sum_sale_avg(item_sold):
    """Считаю среднюю сумму покупок одного товара"""
    avg_sum = 0

    for sold in item_sold:
        avg_sum = count_sum_sale(item_sold) / len(item_sold)
        avg_sum = round(avg_sum)
    return avg_sum


def print_sum_sale_avg_per_phone(phone_sales):
    """Вывожу среднюю сумму покупки каждого товара"""
    avg_sale_per_phone = 0

    for sale in phone_sales:
        sum_avg = count_sum_sale_avg(sale['items_sold'])
        print(f'Среднее количество продаж для товара {sale["product"]} : {sum_avg}')
        # Среднее количество продаж всех товаров
        avg_sale_per_phone += sum_avg
        avg_sale_per_phone = avg_sale_per_phone / len(phone_sales)
        avg_sale_per_phone = round(avg_sale_per_phone)
    print(f'Среднее количество продаж всех товаров: {avg_sale_per_phone}')


def main():
    print_sum_sale_per_phone(phone_sales)
    print_sum_sale_avg_per_phone(phone_sales)

if __name__ == '__main__':
    main()
