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

def discounted(price, discount, max_discount=-23.4):

    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
    except(ValueError):
        raise ValueError("неправильно!")
    except(TypeError):
        raise ValueError("неправильный тип переменной!")

    if max_discount >= 100:
        raise ValueError('Максимальная скидка не должна быть больше 100')

    print(f'{max_discount=} {discount=}')
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)

    return price_with_discount


if __name__ == "__main__":
   # print(discounted(100, 2, 105))
    # print(discounted(100, "3"))
    # print(discounted("100", "4.5"))
    # print(discounted("five", 5))
    print(discounted("сто", "десять"))
    # print(discounted(100.0, 5, "10"))
