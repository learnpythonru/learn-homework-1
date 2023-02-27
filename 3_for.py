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

    phones =  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

# суммарное количество продаж для каждого товара
    def sum_count_sold(solds):
        sum_sold = 0
        for sold in solds:
            sum_sold += sold
        return sum_sold

    for phone in phones:
        print(f'Суммарное количество продаж для {phone["product"]}: {sum_count_sold(phone["items_sold"])}')

# среднее количество продаж для каждого товара
    for phone in phones:
        avg_count_sold = round(sum_count_sold(phone["items_sold"])/len(phone["items_sold"]))
        print(f'Cреднее количество продаж для {phone["product"]}: {avg_count_sold}')

# суммарное количество продаж всех товаров
    sum_all_solds = 0
    for phone in phones:
        sum_all_solds += sum_count_sold(phone["items_sold"])
    print(f'Суммарное количество продаж всех товаров: {sum_all_solds}')

# среднее количество продаж всех товаров
    avg_all_solds = 0
    for phone in phones:
        avg_all_solds = round(sum_all_solds / len(phones))
    print(f'Cреднее количество продаж всех товаров: {avg_all_solds}')

if __name__ == "__main__":
    main()
