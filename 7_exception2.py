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
    except (ValueError, TypeError) as _ex:
        return f'Произошла ошибка {_ex}. Проверьте корректность введенной цены товара {price=}.'

    try:
        discount = abs(float(discount))
    except (ValueError, TypeError) as _ex:
        return f'Произошла ошибка {_ex}. Проверьте корректность введенной скидки на товар {discount=}.'

    try:
        max_discount = abs(int(max_discount))
    except (ValueError, TypeError) as _ex:
        return f'Произошла ошибка {_ex}. Проверьте корректность введенной максимальной ' \
               f'скидки на товар {max_discount=}.'

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
    print(discounted(None, 5, "10.0"))
    print(discounted(100, 5, None))
