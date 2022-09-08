"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""

answer = (input('Как дела? ').lower())
def hello_user(answer):
    while answer != 'хорошо':
        print('Ответьте еще раз!')
        answer = str(input('Как дела? ').lower())
print(hello_user(answer))

