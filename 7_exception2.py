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

def discounted(price=None, discount=None, max_discount=20):
    """
    
    """
    if (price and discount) is None:
        print("Ввеите аргументы(цена и скидка)")
        raise ValueError("Ввеите аргументы(цена и скидка)")
    
    try:
        price = int(price)
    except ValueError:
        try:
            price = float(price)
        except ValueError:
            print("Не верное значение цены")
            raise ValueError("Не верное значение цены")

    try:
        discount = int(discount)
    except ValueError:
        try:
            discount = float(discount)
        except ValueError:
            print("Не верное значение Скидки")
            raise ValueError("Не верное значение Скидки")

    try:
        max_discount = int(max_discount)
    except ValueError:
        try:
            max_discount = float(max_discount)
        except ValueError:
            print("Не верное значение максимальной скидки")
            raise ValueError("Не верное значение максимальной скидки")

    
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
       
    if max_discount >= 100:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)

    
if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))    
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))

