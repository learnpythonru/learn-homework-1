"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold':         [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold':       [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
product_sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


def sales_list_analysis(sales:list)-> tuple(list, list):
    """
    Функция принимет список словарией с продажами товара,
    считает значения по заданию, возвращает 2 списка
    1-й входной список с дополнительными значениями словаря по конкретным товарам
    2-й общие продажи по всем позициям.
    """
    result = []
    all_product_sum = 0
    all_product_count = 0
  
    for index, line in enumerate(sales):
        #вместо sum можно использовать цил for n in line["items_sold"]: и в нем уже аккумулировать значение суммы
        product_sold_sum = sum(line["items_sold"]) 
        all_product_sum += product_sold_sum
        all_product_count += len(line["items_sold"])
        product_avg_sum = product_sold_sum / len(line["items_sold"])
        sales[index]["product_sold_sum"] = product_sold_sum
        sales[index]["product_avg_sum"] = round(product_avg_sum, 2)
  
    result.append({"all_product_sold_sum": all_product_sum, "all_product_avg_sum": round(all_product_sum / all_product_count, 2)})

    return sales , result    


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(sales_list_analysis(product_sales))
 

if __name__ == "__main__":
    main()
