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

sales_of_goods =[
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]


def sum_of_sales_uniq_good(sales: list) -> str:
    """Считает и и выводит суммарное количество продаж для каждого товара"""
    for good in sales:
        name = good["product"]
        total_sale = sum(good["items_sold"])
        return f"{name} продавался {total_sale} раз."


def avg_sales_uniq_good(sales: list) -> str:
    """Считает и выводит среднее количество продаж для каждого товара"""
    for good in sales:
        name = good["product"]
        avg_sale = round(sum(good["items_sold"]) / len(good["items_sold"]))
        return f"{name} продавался {avg_sale} раз в месяц."


def total_sales_all_goods(sales: list) -> str:
    """Считает и выводит суммарное количество продаж всех товаров"""
    total_sales = 0
    for good in sales:
        total_sales += sum(good["items_sold"])
    return f"Суммарное количество продаж: {total_sales}"


def avg_sales_of_all_goods(sales: list) -> str:
    """Считает и выводит среднее количество продаж всех товаров"""
    total_sales = 0
    count_periods_of_sale = 0
    for good in sales:
        total_sales += sum(good["items_sold"])
        count_periods_of_sale += len(good["items_sold"])
    averege = round(total_sales/count_periods_of_sale)
    return f"Среднее количество продаж всех товаров {averege} в месяц"


def main():       
    sum_of_sales_uniq_good(sales_of_goods)
    avg_sales_uniq_good(sales_of_goods)
    total_sales_all_goods(sales_of_goods)
    avg_sales_of_all_goods(sales_of_goods)

    
if __name__ == "__main__":
    main()
