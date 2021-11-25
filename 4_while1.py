"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""


def hello_user():
    while True:
        user_ask = input('Как дела? ')
        if user_ask == 'Хорошо':
            print('Ок')
            break
        else:
            print('{} - это некорректный ответ' .format(user_ask))


def main():
    hello_user()


if __name__ == "__main__":
    main()

