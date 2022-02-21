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

sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def count_item(item_sales):
	sales_sum = 0
	for item in item_sales:
		sales_sum += item
	return sales_sum

def count_item_avg(item_sales):
	sales_sum = 0
	for item in item_sales:
		sales_sum += item
		sales_avg = round(sales_sum / len(item_sales), 2)
	return sales_avg

sales_avg_sum = 0
count_sales_sum = 0
for one_item in sales:
	count_sales = count_item(one_item['items_sold'])
	item_avg = count_item_avg(one_item['items_sold'])
	print(f'Cуммарное количество продаж для {one_item["product"]}: {count_sales}')
	print(f'Cреднее количество продаж для {one_item["product"]}: {item_avg}')
	
	count_sales_sum += count_sales
	sales_avg_sum += item_avg

print(f'Cуммарное количество продаж всех товаров: {count_sales_sum}')
print(f'Среднее количество продаж: {sales_avg_sum}')