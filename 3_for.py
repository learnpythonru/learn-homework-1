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

products = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def quantity(summ = 0, total_summ = 0, avg_total_summ = 0, avg_summ = [], result =[]):
    for i in range(len(products)):
        for j in products[i]['items_sold']:
            summ += j
        result.append(summ)
        summ = 0
    for k in range(len(result)):
        avg_summ.append(int(result[k]/len(products[k]['items_sold'])))
    for g in range(len(result)):
        total_summ += result[g]
    avg_total_summ += (total_summ/len(products))
    return f'Всего каждого товара продано: {result}, средняя стоимость: {avg_summ}, всего товаров продано: {total_summ}, среднее кол-во кажого проданного товара: {avg_total_summ}'
"""
def avg_quantity(summ):
    quantity(summ)
    for i in range(len(products)):
        result[i]
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    action1 = quantity()
    print(action1)

if __name__ == "__main__":
    main()
