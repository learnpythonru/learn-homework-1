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
    """
    Замените pass на ваш код
    """
    try:
      price = abs(float(price))
      discount = abs(float(discount))
    except ValueError:
      return "Цена и скидка должны быть числами!"
    try:
      max_discount = abs(int(max_discount))
    except ValueError:
      return "Максимальная скидка должны быть в виде целого числа!"
    if max_discount > 99:
        return ValueError('Слишком большая максимальная скидка!')
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
