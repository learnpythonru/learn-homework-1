"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по количеству проданных телефонов
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
	sell_data =   [
		{'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
		{'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
		{'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  	]

	for product in sell_data:
		print(product['product'], ': Total sold:', sum(product['items_sold']))
	
	print('-' * 20)

	for product in sell_data:
		print(product['product'], ': Average sold:', round(sum(product['items_sold']) / len(product['items_sold']), 2))

	print('-' * 20)

	counter = 0
	for product in sell_data:
		counter +=  sum(product['items_sold'])
	print('Total overall sold:', counter, 'items')

	print('-' * 20)

	quantity_counter = 0
	len_counter = 0
	for product in sell_data:
		quantity_counter +=  sum(product['items_sold'])
		len_counter += len(product['items_sold'])
	print('Average overall sold:', round(quantity_counter / len_counter, 2), 'items')


if __name__ == "__main__":
    main()

