"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""


def hello_user():
    """
    Замените pass на ваш код
    """
    user_say = input("Как дела?: ")
    while True:
        if user_say.capitalize() == "Хорошо":
            print("Вот и хорошо")
            break
        else:
            print("Ну скажи 'Хорошо'?")
            return hello_user()


if __name__ == "__main__":
    hello_user()
