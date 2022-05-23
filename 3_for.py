"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [
        363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [
        317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [
        343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

from collections import Counter
phones_sold = [
    {'product': 'iPhone 12', 'items_sold': [
        363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [
        317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [
        343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]


def main():
    iphone_sold_sum = 0
    for items in phones_sold[0]['items_sold']:
        iphone_sold_sum += items
    iphone_avg = iphone_sold_sum / len(phones_sold[0]['items_sold'])
    print(
        f'Суммарное количнство продаж iPhone 12: {iphone_sold_sum}, среднее количество продаж: {round(iphone_avg, 1)}')
    Xiaomi_sold_sum = 0
    for items in phones_sold[1]['items_sold']:
        Xiaomi_sold_sum += items
    Xiaomi_avg = Xiaomi_sold_sum / len(phones_sold[1]['items_sold'])
    print(
        f'Суммарное количнство продаж Xiaomi Mi11: {Xiaomi_sold_sum}, среднее количество продаж: {round(Xiaomi_avg, 1)}')
    Samsung_sold_sum = 0
    for items in phones_sold[2]['items_sold']:
        Samsung_sold_sum += items
    Samsung_avg = Samsung_sold_sum / len(phones_sold[2]['items_sold'])
    print(
        f'Суммарное количнство продаж Samsung Galaxy 21: {Samsung_sold_sum}, среднее количество продаж: {round(Samsung_avg, 1)}')
    all_sold_sum = iphone_sold_sum + Xiaomi_sold_sum + Samsung_sold_sum
    print(f'Cуммарное количество продаж всех товаров: {all_sold_sum}')
    all_solds = len(phones_sold[0]['items_sold']) + len(phones_sold[1]
                                                        ['items_sold']) + len(phones_sold[2]['items_sold'])
    all_avg = all_sold_sum / all_solds
    print(f'Cреднее количество продаж всех товаров: {round(all_avg, 1)}')


if __name__ == "__main__":
    main()
