"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""


def hello_user():
    try:
        user_answer = input('Как дела?: ')
        user_answer = user_answer.lower()
        while user_answer == 'хорошо':
            break
        else:
            return hello_user()
    except KeyboardInterrupt:
        print('\nПока!')


if __name__ == "__main__":
    hello_user()
