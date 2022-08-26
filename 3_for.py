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
  phone_sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]}
  ]
  
  print(f"Суммарно продано моделей за год:")
  calc_sales(phone_sales) # Посчитать суммарное количество продаж для каждого товара
  print()

  print(f"Среднее количество продаж в месяц:")
  calc_average_sales(phone_sales) # Посчитать среднее количество продаж для каждого товара
  print()

  print(f"Суммарное количество продаж всех товаров за год:")
  calc_total_sales(phone_sales)
  print()

  print(f"Среднее количество продаж всех товаров в месяц:")
  calc_average_total_sales(phone_sales)
  print()

def calc_sales(data):
  for line in data:
    print(f"{line['product']} - {sum(line['items_sold'])} шт.")

def calc_average_sales(data):
  for line in data:
    print(f"{line['product']} - {sum(line['items_sold'])/len(line['items_sold']):.0f} шт.")

def calc_total_sales(data):
  total = 0
  for line in data:
    total += sum(line['items_sold'])
  
  print(f"{total} шт.")

def calc_average_total_sales(data):
  total = 0
  count = 0
  for line in data:
    total += sum(line['items_sold'])
    count += len(line['items_sold'])
  
  print(f"{total/count:.2f} шт.")

if __name__ == "__main__":
    main()