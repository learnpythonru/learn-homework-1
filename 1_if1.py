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


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = int(input('Введите возраст: '))
    print('Чем должен заниматься пользователь?')
    
    if 0 < age <= 6:
        print ('Учится в детском саду')
    elif 7 <= age <= 18:
        print ('Учится в школе')
    elif 19 <= age <= 22:
        print ('Учится в ВУЗЕ')
    else:
        print ('Работает')

if __name__ == "__main__":
    main()
