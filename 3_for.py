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
scool_list = [{'school_class': '1a', 'scores': [5,4,4,5,4]}, 
              {'school_class': '2a', 'scores': [5,4,5,5,5]},
              {'school_class': '3a', 'scores': [3,4,4,3,2]},
              {'school_class': '4a', 'scores': [3,4,2,5,2]}]

def arithmrtic_mean(lst: list) -> int :  # функция вычисляет среднее арифметическое и округляет результат
    result = int(sum(lst)/len(lst))
    return result

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    global scool_list
    mid_school_score = []

    for scores in scool_list:
        mid_score_in_class = arithmrtic_mean(scores.get("scores"))
        mid_school_score.append(mid_score_in_class)
        print(f'{scores.get("school_class")} - средняя оценка в классе: {mid_score_in_class}')

    print(f'Средняя оценка в школе: {arithmrtic_mean(mid_school_score)}')

    
if __name__ == "__main__":
    main()
