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
    journal = [
        {'school_class': '4-А', 'scores': [5, 5, 4]}, 
        {'school_class': '7-А', 'scores': [2, 3, 5, 2, 4]}, 
        {'school_class': '7-Б', 'scores': [3, 2, 2, 2, 2]}, 
        {'school_class': '8-А', 'scores': [4, 3, 4, 4, 3]}, 
        {'school_class': '9-А', 'scores': [5, 4, 4, 5, 5]}, 
    ]
    sum_school = 0
    count_school = 0
    for item in journal:
        sum_school += sum(item['scores'])
        count_school += len(item['scores'])
        avg = sum(item['scores']) / len(item['scores'])
        print(f'Средний балл {item["school_class"]} составляет {avg:.3}')
    print('=' * 10)
    avg_school = sum_school / count_school
    print(f'Средний балл по школе составляет {avg_school:.3}')

if __name__ == "__main__":
    main()
