"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""


def hello_user():
    while True:
        hello = input("How are you? ")
        if hello == "Fine":
            print("Ok, I'm glad")
            break
        else:
            print(hello)

hello_user()