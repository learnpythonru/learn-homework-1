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
    school_classes = [
                        {'school_class': '4a', 'scores': [3, 4, 4, 5, 1]},
                        {'school_class': '7b', 'scores': [4, 4, 5, 5, 3]},
                        {'school_class': '2c', 'scores': [5, 3, 1, 5, 4]}
                    ]

    school_mean_score = []
    for school_class in school_classes:
        school_mean_score.extend(school_class['scores'])
        print('Class {} mean score = {}'.format(school_class['school_class'], sum(school_class['scores']) / len(school_class['scores'])))

    print('School mean score = {}'.format(sum(school_mean_score) / len(school_mean_score)))

    #pass
    
if __name__ == "__main__":
    main()
