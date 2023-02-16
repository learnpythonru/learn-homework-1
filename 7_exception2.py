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

def try_change_type(object, target_type: type):
    try:
        return abs(target_type(object))
    except (ValueError, TypeError):
        return None


def discounted(price: float, discount: float, max_discount: int=20) -> float:
    try:
        price = try_change_type(price, float)
        discount = try_change_type(discount, float)
        max_discount = try_change_type(max_discount, int)
        if max_discount >= 100:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except (TypeError, ValueError):
        return "Не могу преобразовать значение в число"


if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
