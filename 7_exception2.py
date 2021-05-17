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

def get_discounted_price(price, discount, max_discount=20):
    """
    Замените pass на ваш код
    """
    try:
        if float(discount) < int(max_discount):
            return float(price) - float(price) * float(discount) / 100
        else:
            return float(price) - float(price) * float(max_discount) / 100
    except ValueError:
        print('ValueError')
    except TypeError:
        print('TypeError') #не нужен?

    
    
if __name__ == "__main__":
    print(get_discounted_price(100, 2))
    print(get_discounted_price(100, "3"))
    print(get_discounted_price("100", "4.5"))
    print(get_discounted_price("five", 5))
    print(get_discounted_price("сто", "десять"))
    print(get_discounted_price(100.0, 5, "10"))
