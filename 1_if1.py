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


def user_age():
    age = int(input("Укажите ваш возраст: "))
    answer = ""
    if 0 < age <= 6:
        answer = "Вы должны учиться в детском саду."
    elif 7 <= age <= 17:
        answer = "Вы должны учиться в школе."3
    else:
        answer = "Вы должны учиться в ВУЗе или работать."
    return print(answer)


def main():
    user_age()


if __name__ == "__main__":
    main()
