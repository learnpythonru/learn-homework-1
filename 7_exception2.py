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
import traceback


def discounted(price, discount, max_discount=20):
    try:
        price = float(price)
        discount = float(discount)
        max_discount = int(max_discount)
        if max_discount >= 100:
            raise Exception('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except ValueError:
        traceback_split = traceback.format_exc().split()
        for var in discounted.__code__.co_varnames[:2]:
            if var in traceback_split:
                return f'Неверное значение переменной {var}'
    except TypeError:
        traceback_split = traceback.format_exc().split()
        for var in discounted.__code__.co_varnames[:2]:
            if var in traceback_split:
                return f'Неверный тип переменной {var}'


if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
