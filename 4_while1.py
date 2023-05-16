"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""


def hello_user():

    print('Привет! Введите сообщение: ')

    while True:

        inp: str = input().strip().lower()

        if inp == 'пока':
            get_answer()
            break
        elif inp != 'хорошо':
            print('Как дела?')
        else:
            print('Рад за Вас! (но не от всей души, конечно)')


def get_answer():
    print('Пока!')


if __name__ == '__main__':
    hello_user()
