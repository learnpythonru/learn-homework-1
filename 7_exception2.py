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

def discounted(price: float, discount: float, max_discount: int=20) -> float:
    try:
        price = float(abs(price))        
    except (ValueError, TypeError):
        return ("Не могу преобразовать цену в число!")

    try:        
        discount = float(abs(discount))
    except (ValueError, TypeError):
        return ("Не могу преобразовать скидку в число!")

    try:    
        max_discount = int(abs(max_discount))
    except (ValueError, TypeError):
        return "Не могу преобразовать max скидку в число"

    if max_discount >= 100:
        raise ValueError('Слишком большая максимальная скидка')
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
