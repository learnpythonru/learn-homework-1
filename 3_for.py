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

scores_table = [
    {'school_class': '1а',
     'scores': [3, 4, 5, 5, 4, 3, 4]
     },
    {'school_class': '2б',
     'scores': [4, 4, 3, 2, 4, 5]
     },
    {'school_class': '3б',
     'scores': [2, 4, 5, 3, 3, 4]
     },
    {'school_class': '4в',
     'scores': [3, 5, 5, 4, 5, 4, 5]
     },
]


def get_average(scores):
    summary = 0
    for score in scores:
        summary += score
    return summary / len(scores)


def main():
    avg_by_school = []
    for class_table in scores_table:
        avg_by_class = get_average(class_table["scores"])
        print(f'Class: {class_table["school_class"]}, Avg score: {round(avg_by_class, 2)}')
        avg_by_school.append(avg_by_class)
    print('----------------------------')
    print(f'Avg score by school: {round(get_average(avg_by_school), 2)}')


if __name__ == "__main__":
    main()
