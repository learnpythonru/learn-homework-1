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

phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]


def main(phone_sold):
    scores_sum = 0
    for score in phone_sold:
        scores_sum += score
    scores_avg = scores_sum / len(phone_sold)
    print(f"Суммарно {one_mark['product']} проданно {scores_sum}")
    return scores_avg


for one_mark in phones:
    mark_score_avg = main(one_mark['items_sold'])
    print(f"Средние продажи на марку телефона {one_mark['product']}: {mark_score_avg}.")

avg_scores_sum = 0

for one_mark in phones:
    avg_scores_sum += main(one_mark["items_sold"])

mark_avg = avg_scores_sum / len(phones)
print(f"В среднем по каждой марке {mark_avg}. В среднем продано всего {avg_scores_sum}")

try:
    if __name__ == "__main__":
        main()
except TypeError:
    print("Подсчет закончен")
