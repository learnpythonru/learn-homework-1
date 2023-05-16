"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

from typing import Optional


def define_occupation_by_age(age: int) -> Optional[str]:
    """
    Function get user age and define their expected occupation
    """
    if 0 <= age < 7:
        return 'учиться в детском саду'
    elif 7 <= age < 17:
        return 'учиться в школе'
    elif 17 <= age < 24:
        return 'учиться в ВУЗе'
    elif 24 <= age < 65:
        return 'работать'
    elif 65 <= age <= 120:
        return 'отдыхать (быть пенсионером)'


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    while True:
        user_age = int(input('Введите возраст (от 0 до 120 лет): '))
        if user_age < 0 or user_age > 120:
            print('Возраст введён некорректно, попробуйте ещё раз')
        else:
            user_expected_occupation = define_occupation_by_age(user_age)
            print(f'Ожидается, что в этом возрасте человек должен {user_expected_occupation}')


if __name__ == "__main__":
    main()
