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

    phones = [
        {'product': 'iPhone 12', 'items_sold': [
            363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [
            317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [
            343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

    def count_sum(items_list):
        items_sum = 0
        for item in items_list:
            items_sum += item
        return items_sum

    phones_sum = 0
    for phone in phones:
        phone['sum_sold'] = count_sum(phone['items_sold'])
        phone_sold_avg = int(phone['sum_sold'] / len(phone['items_sold']))
        phones_sum += phone['sum_sold']
        print(
            f"Суммарное количество продаж {phone['product']}: {phone['sum_sold']}")
        print(
            f"Среднее количество продаж {phone['product']}: {phone_sold_avg}", end='\n\n')
    print(f"Всего телефонов продано: {phones_sum}")
    phones_avg = int(phones_sum / len(phones))
    print(f"В среднем телефонов продано: {phones_avg}")


if __name__ == "__main__":
    main()
