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


def main(school_classes):
    scores_sum = 0
    for a_clas in school_classes:
        scores_sum += sum(a_clas["scores"])
    return scores_sum / len(school_classes)


def middle_scores(school_classes):
    for a_clas in scoole_class_with_scores:
        print(f"Класс {a_clas['school_class']} имеет средний бал равный: {sum(a_clas['scores']) / len(a_clas['scores'])}")


scoole_class_with_scores = [
  {"school_class": "4a", "scores": [3, 2, 4, 5, 1, 2]},
  {"school_class": "5a", "scores": [5, 2, 1, 5, 2, 2]},
  {"school_class": "6a", "scores": [3, 3, 4, 3, 4, 2]},
  {"school_class": "7a", "scores": [2, 2, 2, 5, 2, 2]},
  {"school_class": "8a", "scores": [5, 5, 4, 5, 4, 2]},
  {"school_class": "9a", "scores": [3, 2, 4, 5, 2, 2]}
]

if __name__ == "__main__":
    print(f"Средний бал по всей школе: {main(scoole_class_with_scores)}")
    middle_scores(scoole_class_with_scores)
