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

import sys


def stderr_log(msg):
    sys.stderr.write("ERR: " + msg + "\n")


def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
    except (ValueError, TypeError) as e:
        stderr_log("Illegal price argument: " + e.args[0])
        return -1

    try:
        discount = abs(float(discount))
    except (ValueError, TypeError) as e:
        stderr_log("Illegal discount argument " + e.args[0])
        return -1

    try:
        max_discount = abs(int(max_discount))
    except (ValueError, TypeError) as e:
        stderr_log("Illegal max_discount argument " + e.args[0])
        return -1

    try:
        if max_discount > 99:
            raise ValueError('Discount is too high')
    except ValueError as e:
        stderr_log(e.args[0])
        return -1

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
    print(discounted(100.0, 5, 100))
