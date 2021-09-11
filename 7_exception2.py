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

    price = float(abs(price))
    discount = float(abs(discount))
    max_discount = int(abs(max_discount))
    if max_discount >= 100:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)

def print_discounted(price, discount, max_discount=20):
    try:
        print(discounted(price, discount, max_discount))
    except (TypeError, ValueError) as err:
        print(err)

def main():

    print_discounted(100, 2)
    print_discounted(100, "3")
    print_discounted("100", "4.5")
    print_discounted("five", 5)
    print_discounted("сто", "десять")
    print_discounted(100.0, 5, "10")

if __name__ == "__main__":
    main()
