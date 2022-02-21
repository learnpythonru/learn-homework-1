"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""


def hello_user():
    user_answer = input('Как дела?: ')
    user_answer = user_answer.lower()
    while user_answer == 'хорошо':
        break
    else:
        hello_user()


hello_user()
