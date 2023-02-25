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

tovar =  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def summa(items_sold):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    sum_phone = 0
    for item in items_sold:
        sum_phone += item
    return sum_phone

 


def avg(items_sold):
    avg = summa(items_sold) / len(items_sold)
    return avg


if __name__ == "__main__":
    total_sum = 0

    for one_phone in tovar:
        sum_item_sold = summa(one_phone['items_sold'])
        print(f'Всего продаж: {sum_item_sold}')
        total_sum += sum_item_sold

    for avg_phone in tovar:
        avg_item_sold = avg(avg_phone['items_sold'])
        print(f'Среднее количество продаж: {round(avg_item_sold, 2)}')

    total_avg = total_sum / len(tovar)

    print(f'Всего продано: {total_sum}')
    print(f'Общее среднее количество продаж: {total_avg}')

    