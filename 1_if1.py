age = int(input('Введите ваш возраст: '))

def work(age):
# Для упрощения функции , делаем ее более линейной, убираем лишние Else и Elif
    if age <= 6:
        return 'Вы учитесь в детском саду'

    if age <= 16:
        return 'Вы учитесь в школе'

    if age <= 21:
        return 'Вы учитесь в ВУЗе'

    return 'Вы работаете'

def main():
    if __name__ == "__main__":
        main()

print(work(age))
