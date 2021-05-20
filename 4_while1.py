"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    answer = ''
    while answer != 'Хорошо':
        answer = input('Как дела? ')
    print('Рад за Вас')


def hello_user2():
    while True:
        if input('Как дела? ') == 'Хорошо':
            break
    print('Рад за Вас')


def hello_user3():
    while input('Как дела? ') != 'Хорошо':
        pass
    print('Рад за Вас')


if __name__ == "__main__":
    hello_user3()  # Вариант 3 мне нравится больше других
