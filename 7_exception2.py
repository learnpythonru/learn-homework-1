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

# from lesson 6 (функции)
def discounted(price, discount, max_discount=20):
    try: # добавляем к стандартному переводу типов
        price = abs(price)
        discount = abs(discount)
        max_discount = abs(max_discount)
        if max_discount >= 100:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
#product = {'name': 'Samsung Galaxy S21', 'price': 50000.0, 'discount': 5}
#product['price_discounted'] = discounted(product['price'], product['discount'])
#print(product)
    except (ValueError, TypeError): # перехват исключений
        print('Некорректные данные') # 5 из 6
    
if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
