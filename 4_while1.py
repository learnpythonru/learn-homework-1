"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""


user_say = str(input('Как дела? '))

def hello_user(user_say):
  while True:

    if user_say.lower() == 'хорошо':
      break

    else:
      user_say = input('Как дела? ')

hello_user(user_say)
