"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""


def hello_user(how = None):
    """
    Замените pass на ваш код
    """
    while how != 'Хорошо':
        print('Привет, как дела?')
        how = str(input())


if __name__ == "__main__":
    hello_user()
