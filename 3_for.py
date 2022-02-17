"""
Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]
#Блок задания №1
print('\nУсловие №1:')
def count_summ_product (items_sold):
    solds_summ = 0
    for sold in items_sold:
        solds_summ += sold
    return solds_summ 

product_summ = 0
for one_phone in phones:
    phone_summ = count_summ_product(one_phone['items_sold'])
    print(f'Суммарное количество продаж для {one_phone["product"]}: {phone_summ}') 
    product_summ += phone_summ

print('\nУсловие №3:')
product_summ = round(product_summ , 1)
print(f'Всего продано товаров: {product_summ}') 

#Блок задания №2
print('\nУсловие №2:')
def count_summ_product (items_sold):
    solds_summ = 0
    for sold in items_sold:
        solds_summ += sold
    return solds_summ / len(items_sold)

product_summ = 0
for one_phone in phones:
    phone_summ = count_summ_product(one_phone['items_sold'])
    print(f'Среднее количество продаж для {one_phone["product"]}: {phone_summ}')
    product_summ += phone_summ

print('\nУсловие №4:')
product_summ = round(product_summ / len(phones) , 1)
print(f'Среднее количество всех проданных: {product_summ}')

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass
    
if __name__ == "__main__":
    main()
