"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""

user_say = str(input('Как дела? '))

def hello_user(user_say):

    try:
        while True:

         if user_say.lower() == 'хорошо':
            break

        else:
            user_say = input('Как дела? ')

    except KeyboardInterrupt:
        print('Пока!')


if __name__ == "__main__":
    hello_user(user_say)
