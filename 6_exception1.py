"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""


def hello_user():
    """
    Замените pass на ваш код
    """

    while True:
        try:
            txt = input('Как дела? ')
            if txt.lower() == 'хорошо':
                break
            else:
                print('Скажи еще что-нибудь')
        except KeyboardInterrupt:
            print('Пока')
            break



if __name__ == "__main__":
    hello_user()
