def discounted(price: int | str, discount: int | str, max_discount: int | str =20) -> float:

    try:
        price: float = abs(float(price))
        discount: float = abs(float(discount))
        max_discount: int = abs(int(max_discount))
    except ValueError or TypeError:
        return 'Неверное значение!'
    else:
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
