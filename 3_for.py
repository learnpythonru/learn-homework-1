phone_sold = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]

def sale_avg(phone_items_sold):    #среднее количество продаж для каждого товара (функция)
  items_sold_sum = 0               
  for items in phone_items_sold:   
    items_sold_sum += items
  return round(items_sold_sum / len(phone_items_sold), 1)
   
items_sold_avg = 0 

for one_phone in phone_sold: #цикл для каждого проданного товара
  phone_sold_avg = sale_avg(one_phone['items_sold'])
  print(f'Среднее количество продаж для каждого товара: {one_phone["product"]}: {phone_sold_avg}')
  items_sold_avg += phone_sold_avg
  items_avg = round(items_sold_avg/ len(phone_sold), 2)
print(f'Среднее количество продаж всех товаров: {items_avg}')

def sale_sum(phone_items_sold):    #суммарное количество продаж для каждого товара (функция)
  items_sold_sum = 0               
  for items in phone_items_sold:   
    items_sold_sum += items
  return items_sold_sum 

items_sold_sum = 0 

for phone_items_sum in phone_sold: #цикл для общего количества каждого проданного товара
  phone_sold_sum = sale_sum(phone_items_sum['items_sold'])
  print(f'Суммарное количество продаж для каждого товара: {phone_items_sum["product"]}: {phone_sold_sum}')
  items_sold_sum += phone_sold_sum
print(f'Суммарное количество продаж всех товаров: {items_sold_sum}')






