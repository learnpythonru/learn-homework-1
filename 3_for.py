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

def sum_phone_store(phone_sale_arr):
  pnone_sale_summ = 0
  for sale in phone_sale_arr:
    pnone_sale_summ += sale
  return pnone_sale_summ
  
def avg_phone_store(phone_sale_arr):
  pnone_sale_summ = 0
  for sale in phone_sale_arr:
    pnone_sale_summ += sale
  return pnone_sale_summ / len(phone_sale_arr) 


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    #Посчитать и вывести суммарное количество продаж для каждого товара
    sum = 0
    for phone in phone_store:  
      sum = sum_phone_store(phone['items_sold'])
      print(f'Суммарное количество проданных телефонов марки {phone["product"]}: {sum} \n') 

    #Посчитать и вывести среднее количество продаж для каждого товара
    avg = 0
    for phone in phone_store:  
          avg = round(avg_phone_store(phone['items_sold']), 2)
          print(f'Среднее количество проданных телефонов марки {phone["product"]}: {avg} \n')
    #Посчитать и вывести суммарное количество продаж всех товаров
    sum = 0
    for phone in phone_store:  
      sum += sum_phone_store(phone['items_sold'])
    print(f'Cуммарное количество продаж всех товаров: {sum} \n') 

    #Посчитать и вывести среднее количество продаж всех товаров
    sum = 0
    avg_all = 0
    for phone in phone_store:  
      sum += sum_phone_store(phone['items_sold'])
    avg_all = round(sum / len(phone_store), 2)
    print(f'Среднее количество продаж всех товаров: {avg_all} \n') 
    
    
if __name__ == "__main__":
    main()
