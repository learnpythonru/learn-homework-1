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
    telephones = [
                  {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
                  {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
                  {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]}
  ]
    sum_count_items_sold = 0
    count_avg_all_tel = 0
    for sold in telephones:
        print(f'Суммарное количество продаж для {sold["product"]}: {sum(sold["items_sold"])}')
        sum_count_items_sold += sum(sold['items_sold'])
        count_avg_tel = sum(sold["items_sold"]) / len(sold["items_sold"])
        print(f'среднее количество продаж для {sold["product"]}: {count_avg_tel}' )
        count_avg_all_tel = sum_count_items_sold / sum(sold['product'])
    
    print(f'среднее количество продаж всех товаров: ', count_avg_all_tel)    
    print(f'суммарное количество продаж всех товаров: ', sum_count_items_sold)
    


if __name__ == "__main__":
    main()
