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

stock = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def main():
  def item_sum(quantity):
    sold_sum = 0
    for item in quantity:
     sold_sum += item
    return sold_sum

all_prod_sum = 0
for one_product in stock:
  product_sum = product_sum(one_product['items_sold'])
  print(product_sum)
  all_prod_sum += product_sum
  print(all_prod_sum)


def item_avg(quantity):
  sell_sum = 0
  for item in quantity:
    sell_sum += item
    avg_prod = sell_sum / len(quantity)  
  return avg_prod

all_prod_avg = 0
for one_product in stock:
  product_avg = item_avg(one_product['items_sold'])
  print(product_avg)

all_prod_avg = product_avg / len(stock)
print(all_prod_avg)
    
if __name__ == "__main__":
    main()
