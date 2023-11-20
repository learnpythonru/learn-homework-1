"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
"""
lst_phone = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
"""
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
def sum_list_prod(lst):
    for product in lst:
        print('Cуммарное количество продаж ',product['product'],'-  ',sum(product['items_sold']))

def average_lst(lst):
    for product in lst:
        avrge_lst = round((sum(product['items_sold'])/len(product['items_sold'])),2)
        print('Cреднее количество продаж ', product['product'],'- ',avrge_lst)

def sum_sold(lst):
    s = 0
    for product in lst:
        a = sum(product['items_sold'])
        s += a
    print('Cуммарное количество продаж всех товаров ', s)

def avrge_sold(lst):
    
    for i in lst:
        count = 0
        a = 0
        avrge = round((sum(i['items_sold'])/len(i['items_sold'])),2)
        a += avrge
        count += 1
    print('Cреднее количество продаж всех товаров ', a/count)

def main():
    sum_list_prod(lst_phone)
    average_lst(lst_phone)
    sum_sold(lst_phone)
    avrge_sold(lst_phone)

    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    #pass
    
if __name__ == "__main__":
    main()
