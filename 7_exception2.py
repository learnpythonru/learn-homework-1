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

def discounted(price, discount, max_discount=20):
  try:
    price1 = float(price)
    discount1 = float(discount)
    max_discount1 = int(max_discount) 
    if max_discount1 > 99:
        raise ValueError('Слишком большая максимальная скидка')
    else:
        try:
             price1 = float(price)
             discount1 = float(discount)
             return price1 - (price1 * discount1 / 100)
        except TypeError:
             return "не те данные"
  except ValueError:
    return "Не коректный тип входных данные"


    
if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
