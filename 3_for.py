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

from ast import main


def main():
    phones = [
        {
            "product": "iPhone 12",
            "items_sold": [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186],
        },
        {
            "product": "Xiaomi Mi11",
            "items_sold": [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316],
        },
        {
            "product": "Samsung Galaxy 21",
            "items_sold": [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247],
        },
    ]
    scores_sum = 0
    all_phones = 0

    for sold in phones:
        all_phones_summ = sum(sold["items_sold"])
        print(f"Суммарное колличество продаж для каждого товара {all_phones_summ}")
        scores_sum += sum(sold["items_sold"])
        if len(sold["items_sold"]) > 0:
            all_summ = sum(sold["items_sold"]) / len(sold["items_sold"])
            print(f"Среднее количество продаж для кадого товара {all_summ}")
            all_phones += all_summ
    print(f"Cуммарное количество продаж всех товаров {scores_sum}")
    print(f"Среднее количество продаж всех товаров {all_phones}")


if __name__ == "__main__":
    main()
