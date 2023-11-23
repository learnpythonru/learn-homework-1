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
        price = abs(float(price))
    except (ValueError, TypeError):
        print(f'Для параметра "price" передан некорректный тип данных {price}')
        return
    try:
        discount = abs(float(discount))
    except (ValueError, TypeError):
        print(f'Для параметра "discount" передан некорректный тип данных {discount}')
        return
    try:
        max_discount = abs(float(max_discount))
    except (ValueError, TypeError):
        print(
            f'Для параметра "max_discount" передан некорректный тип данных {max_discount}'
        )
        return
    if max_discount >= 100:
        raise ValueError("Слишком большая максимальная скидка")
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
