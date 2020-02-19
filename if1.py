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
    age = int(input("Insert user age "))
    if age <= 0:
        print("User even not born, wtf you thinking about?")
    elif 1 < age < 3:
        print("User age is {}, he/she stay at home with mother".format(age))
    elif 4 < age < 6:
        print("User age is {}, he/she have to be in kindergarden".format(age))
    elif 7 < age < 18:
        print("User age is {}, he/she have to be in school".format(age))
    elif 19 < age < 22:
        print("User age is {}, if he/she smart  study at university. Otherwise probably in army".format(age))
    elif 22 < age < 65:
        print("User age is {}, he probably working".format(age))
    else:
        print("User age is {}. If user keep making sport he could be alive and taking his pension funds for "
              "survival".format(age))

if __name__ == "__main__":
    main()
