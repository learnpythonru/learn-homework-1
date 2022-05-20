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
phone_store =   [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]



def print_sum_stores(phone_stores):
  sum_phone_sale = 0
  for phone in phone_store:  
    sum_phone_sale = sum(phone['items_sold'])
    print(f'Суммарное количество проданных телефонов марки {phone["product"]}: {sum_phone_sale} \n') 

def print_avg_stores(phone_stores):
  avg_phone_sale = 0
  for phone in phone_store:  
    avg_phone_sale = round(sum(phone['items_sold']) / len(phone['items_sold']), 2)
    print(f'Среднее количество проданных телефонов марки {phone["product"]}: {avg_phone_sale} \n')

def print_sum_stores_all_model(phone_stores):
  sum_phone_sale = 0
  for phone in phone_store:  
    sum_phone_sale += sum(phone['items_sold'])
  print(f'Cуммарное количество продаж всех товаров: {sum_phone_sale} \n') 

def print_avg_stores_all_model(phone_stores):
  sum_phone_sale = 0
  avg_phone_sale_all = 0
  for phone in phone_store:  
    sum_phone_sale += sum(phone['items_sold'])
  avg_phone_sale_all = round(sum_phone_sale / len(phone_store), 2)
  print(f'Среднее количество продаж всех товаров: {avg_phone_sale_all} \n') 


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    
    print_sum_stores(phone_store)    
    print_avg_stores(phone_store)    
    print_sum_stores_all_model(phone_store)    
    print_avg_stores_all_model(phone_store)


    
    
if __name__ == "__main__":
    main()
