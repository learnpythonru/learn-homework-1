"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""
phone1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'discount': 15}
phone2 = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 10}
phone3 = {'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}




def discounted(price, discount, max_discount=50, name=''):
    

    try:
        price = abs(float(price))
    except(TypeError, ValueError):
        print('Введены неверные параметры')
        price = 0
    
    try:
        discount = abs(float(discount))
    except(TypeError, ValueError):
        print('Введены неверные параметры')
        discount = 0        
    
    try:    
        max_discount = abs(int(max_discount))
    except(TypeError, ValueError):
        print('Введены неверные параметры')
        max_discount = 0

    
    
    
    if max_discount > 99:
        raise ValueError('Максимальная скидка не может быть больше 99%')

    if discount >= max_discount or 'iphone' in name.lower() or not name:
        price_with_discount = price
    
    else:    
        price_with_discount = price - (price * discount / 100)
    
    return(price_with_discount)


        
             

if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
