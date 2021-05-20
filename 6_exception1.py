"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""


def hello_user():
    try:
        user_says = ''
        while user_says != 'Хорошо':
            user_says = input('Как дела?: ')
    except KeyboardInterrupt:
        print('\nПока!')


if __name__ == "__main__":
    hello_user()
