sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]

def count_sales(sale_list): #функция count_sales с аргументом sale_list
    sales_sum = 0 #знчение переменной sales_sum равно нолю
    for count in sale_list: #для переменной count в sale_list
        sales_sum += count #прибавляй к значению переменной sales_sum значение переменной count и записывай его в sales_sum
    return sales_sum / len(sale_list) #возвращай значение sales_sum деленное на длину списка sale_list

school_avg_sum = 0
for one_item in sales:#для переменной one_item в sales
    total_sales_sum = count_sales(one_item['items_sold'])
    print(f"Средняя оценка для продукта {one_item['product']}: {total_sales_sum}")
    school_avg_sum += total_sales_sum
    print(f"Средняя оценка для школы: {school_avg_sum / len(sales)}")

if __name__ == "__count_sales__":
    count_sales()