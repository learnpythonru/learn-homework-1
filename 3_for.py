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

sells_list = [{'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
              {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
              {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},]

def sell_analysis(items_sold: list) -> dict:
    sum = 0
    for i in items_sold:
        sum += i
    average = sum / len(items_sold)
    res = {'summ': sum, 'average': average, 'sell_days': len(items_sold)}
    return res

def main():
    all_sum = 0
    all_sell_days = 0
    for phone in sells_list:
        sells = sell_analysis(phone['items_sold'])
        print(f"Product {phone['product']} was sold {sells['summ']} times with average {sells['average']}")
        all_sum += sells['summ']
        if sells['sell_days'] > all_sell_days:
            all_sell_days = sells['sell_days']
    print(f"All products sales:{all_sum}\nAverage sells of all products:{all_sum/all_sell_days}")

    
if __name__ == "__main__":
    main()
