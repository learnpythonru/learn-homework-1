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
def phone_sales_amount(items_sold):
    total_sales, number_of_sales = 0, 0
    for sale in items_sold:
        total_sales += sale
        number_of_sales += 1
    average_sales = total_sales // number_of_sales
    return total_sales, average_sales
def total_number_of_sales_for_each_product(phone, total_sales):
    return f'Всего продаж {phone}: {total_sales}'
def average_number_of_sales_for_each_product(phone, average_sales):
    return f'Средние количетсво продаж {phone}: {average_sales}'
def total_and_average_number_of_phone_sales(sales_figures):
    total_sales, number_of_sales = 0, 0
    for dict in sales_figures:
        total_sales += phone_sales_amount(dict['items_sold'])[0]
        number_of_sales += 1
    average_number_of_phone_sales = total_sales // number_of_sales
    return total_sales, average_number_of_phone_sales


if __name__ == "__main__":
    sales_figures =  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
    for dict in sales_figures:
        phone = dict['product']
        total_sales = phone_sales_amount(dict['items_sold'])[0]
        print(total_number_of_sales_for_each_product(phone, total_sales))
    for dict in sales_figures:
        phone = dict['product']
        average_sales = phone_sales_amount(dict['items_sold'])[1]
        print(average_number_of_sales_for_each_product(phone, average_sales))
    print(f'Сумммарное количество продаж всех товаров: {total_and_average_number_of_phone_sales(sales_figures)[0]}')
    print(f'Средние количество продаж всех товаров: {total_and_average_number_of_phone_sales(sales_figures)[1]}')