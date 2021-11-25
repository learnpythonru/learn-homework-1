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

my_list = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


def count_sales(brand_sales):
    sales_sum = 0
    for sale in brand_sales:
        sales_sum += sale
    return sales_sum


def count_average_sales(brand_sales):
    sales_sum = 0
    average_sales = 0
    for sale in brand_sales:
        sales_sum += sale
        average_sales = sales_sum/len(brand_sales)
    return average_sales


def summation_sale():
    for one_brand in my_list:
        brands_sales = count_sales(one_brand['items_sold'])
        print(f"Продажи бренда {one_brand['product']}: {brands_sales}")


def summation_avg_sale():
    for one_brand in my_list:
        brands_sales = count_average_sales(one_brand['items_sold'])
        print(f"Среднее количество продаж бренда {one_brand['product']}: {brands_sales}")


def all_summation_sale():
    all_sales = 0
    for one_brand in my_list:
        brands_sales = count_sales(one_brand['items_sold'])
        all_sales += brands_sales
    print(f"Продажи всех брендов : {all_sales}")


def all_avg_summation_sale():
    all_avg_sales = 0
    for one_brand in my_list:
        brands_sales = count_average_sales(one_brand['items_sold'])
        all_avg_sales += brands_sales
    print(f"Среднее количество продаж всех брендов : {all_avg_sales}")


def main():
    print(summation_sale())
    print(summation_avg_sale())
    print(all_summation_sale())
    print(all_avg_summation_sale())


if __name__ == "__main__":
    main()

