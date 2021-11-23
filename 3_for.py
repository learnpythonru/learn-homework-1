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
school_data = [
    {"school_class": "4a", "scores": [3, 4, 4, 5, 2]},
    {"school_class": "4b", "scores": [3, 5, 5, 5, 5]},
    {"school_class": "5", "scores": [3, 3, 4, 3, 2]},
    {"school_class": "5b", "scores": [3, 3, 3]},
]

def school_estim(data_dict):
    class_nb = len(school_data)  # number of classes in school
    score_school_m = 0
    score_nb = 0
    for school_c in data_dict:
        score_m = sum(school_c["scores"]) / len((school_c["scores"]))
        score_school_m += sum(school_c["scores"])
        score_nb += len((school_c["scores"]))
        print(f"Average score in {school_c['school_class']} is {score_m}")
    average_school_scr = score_school_m / score_nb
    print('Average score in school is', average_school_scr)
    
if __name__ == "__main__":
    school_estim(school_data)
