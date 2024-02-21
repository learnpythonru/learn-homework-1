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
        price = float(abs(price))
        discount = float(abs(discount))
        max_discount = int(abs(max_discount))
    except(ValueError, TypeError):
        print("Указать соответствующий тип данных, иначе скидка приравнивается к нулю, а цена к 100")
        price = 100
        discount = 0
        max_discount = 0
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
