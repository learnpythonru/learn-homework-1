"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.

# lesson 6 (функции)
def discounted(price, discount, max_discount=20):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
         return price - (price * discount / 100)
product = {'name': 'Samsung Galaxy S21', 'price': 50000.0, 'discount': 5}
product['price_discounted'] = discounted(product['price'], product['discount'])
print(product)

#Задание 1
def get_summ(one, two, delimiter ='&'):
    summ = str.upper(one) + delimiter + str.upper(two) #сложение с переводом строки в заглавные буквы(верхний регистр), либо использовать str.title для заглавных первых букв
    print (summ)
data = {'one': 'learn', 'two': 'python'} # словарь с исходными данными для функции
result = get_summ(data['one'], data['two']) # выполнение функции для данного списка

#Задание 2
def format_price(price):
    integer = str(int(price))
    message = f'Цена: {integer} руб.'
    print (message)
price = 56.24
format_price(price)



"""

def discounted(price, discount, max_discount=20):
    """
    Замените pass на ваш код
    """
    pass
    
if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
