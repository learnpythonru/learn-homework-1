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



stock =  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
# ЗАДВАИВАЕТ ИТОГОВЫЕ ПРОДАЖИ ВСЕХ И ОДНОГО БРЕНДА, А ТАК ВСЁ ОК

def main():
    index = 0
    total_sum = 0
    aver_sum = 0
    for key in stock[index]:
        while index   < len(stock)  :


                sum_one_brand = sum(stock[index]['items_sold'])
                print(f"Всего продано {stock[index]['product']} - {sum_one_brand} штук .")

                average_one_brand = int(sum(stock[index]['items_sold']) / len(stock[index]['items_sold']))
                print(f"Cреднее количество продаж {stock[index]['product']} - {average_one_brand} штук.")
                index += 1

                total_sum += sum_one_brand
                aver_sum =  int(total_sum/len(stock))

        print(f"Суммарное количество продаж всех товаров {total_sum} штук")
        print(f"Cреднее количество продаж всех товаров {aver_sum} штук каждого бренда ")

        

if __name__ == "__main__":
    main()