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
sales =   [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
      ]
def main():
    major_sales = 0
    major_average_sales = 0

    for item in range(len(sales)): # перебор по каждой строке
        print ({sales[item]['product']}) # значение ключа 'product' в словаре sales

        total_sales = 0
        for item_sales in range(len(sales[item]['items_sold'])):
            total_sales = total_sales + (sales[item]['items_sold'][item_sales]) # общее количество продаж для конкретной модели
            average_sales = float(total_sales) / len(sales[item]['items_sold']) # среднее количество продаж для конкретной модели
        print (f'Общее количество продаж: {total_sales}')
        print (f'Среднее количество продаж: {average_sales}')
        major_sales += total_sales # общее кол-во продаж для всех моделей
        major_average_sales += average_sales # среднее кол-во продаж для всех моделей
    
    print (f'Суммарное количество продаж всех товаров: {major_sales}')
    print (f'Cреднее количество продаж всех товаров: {major_average_sales}')

if __name__ == "__main__":
    main()
# Непросто было вытащить данные из словаря списков
# Натыкался на local variable ‘x’ referenced before assignment
# Результат получен, но надо допилить нормальный вывод данных.