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
phones_sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
# sum of sales for 1 phone model
def sum_model_sales(sales_dict):
    return sum(sales_dict['items_sold'])

# average sales for 1 phone model
def avg_model_sales(sales_dict):
    return sum_model_sales(sales_dict) / len(sales_dict['items_sold'])

# calculate and print average and sum of sales for each model
def print_sum_avg_phone_sales(sales_list):
    for phone in sales_list:
        print(f"{phone['product']} total sold: {sum_model_sales(phone):.2f}")
        print(f"{phone['product']} sold on average: {avg_model_sales(phone):.2f}")

# calculate and print average and sum of all sales
def print_sum_avg_all_sales(sales_list):
    total_sum = 0
    total_len = 0
    for phone in sales_list:
        total_sum += sum_model_sales(phone)
        total_len += len(phone['items_sold'])
    print(f"Total sales of all phone models: {total_sum}")
    print(f"Average sales of all phone models: {(total_sum / total_len):.2f}")




def main():

    print_sum_avg_phone_sales(phones_sales)
    print_sum_avg_all_sales(phones_sales)
    
if __name__ == "__main__":
    main()
