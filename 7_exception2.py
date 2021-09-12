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


def process_arguments(price, discount, max_discount=20):
    try:
        float(price)
        float(discount)
        int(max_discount)
    except (ValueError, TypeError):
        print('Please enter a valid value')
        
def get_discounted_price(price, discount, max_discount=20):
  
    process_arguments(price, discount, max_discount=20)

    if max_discount >= 100:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)

if __name__ == "__main__":
   print(get_discounted_price(40, 14))
  #  print(get_discounted_price('A', 14))
  #  print(get_discounted_price(40, 'A'))
  #  print(get_discounted_price(40, 30, 14.8))
