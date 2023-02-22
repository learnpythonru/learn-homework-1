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

def years(age):
    res = ''
    if age < 7:
        res = 'детский сад'
    elif age < 18:
        res = 'школа'
    elif age < 65:
        res = 'работа'
    else:
        res = 'пенсия'
    return res


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = input('Введите ваш возраст: ')
    while True:
        if age.isdigit():
            age = int(age)
            occ = years(age)
            print('Вашим основным занятием является - ' + occ)
            break
        else:
            age = input('Введите ваш возраст  цифрами: ')

if __name__ == "__main__":
    main()
