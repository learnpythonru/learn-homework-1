"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    running = True
    while running:
        hello = input('Как дела? ')
        if hello != 'Хорошо':
            continue
        else:
            break


print(hello_user())
