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


def determine_age(digit):
    if digit < 0:
        user = 'Person was not born. Wrong input. Input age from 3 to 65.'
    elif 3 <= digit <= 6:
        user = 'go to kindergarden'
    elif 6 < digit <= 16:
        user = 'go to school'
    elif 16 < digit <= 23:
        user = 'go to univercity'
    elif 23 < digit <= 65:
        user = 'go to work'
    else:
        user = 'Wrong input. Input age from 3 to 65.'

    return user


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = int(input('Input person age from 3 to 65: > '))
    result = determine_age(age)
    print(result)


if __name__ == "__main__":
    main()