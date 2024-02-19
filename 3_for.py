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
    stock = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
        ]

    def sum_each_items_sold(model_items_sold):
        items_sold_sum = 0
        for items in model_items_sold:
            items_sold_sum += items
        return items_sold_sum

    def avg_sum_each_items_sold(model_items_sold):
        items_sold_sum = 0
        for items in model_items_sold:
            items_sold_sum += items
        return items_sold_sum / len(model_items_sold)

    sum_all_models = 0
    avg_all_models = 0
    for one_model in stock:
        items_sum = sum_each_items_sold(one_model['items_sold'])
        items_avg_model = avg_sum_each_items_sold(one_model['items_sold'])
        print(f'Суммарное количество продаж {one_model["product"]}: {items_sum}')
        print(f'Среднее количество продаж {one_model["product"]}: {items_avg_model}')
        sum_all_models += items_sum
        avg_all_models += items_avg_model
    print(f'Суммарное количество продаж всех товаров: {sum_all_models}')
    print(f'Среднее количество продаж всех товаров: {avg_all_models}')

if __name__ == "__main__":
    main()
