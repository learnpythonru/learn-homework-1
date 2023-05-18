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
    try:
        text = input('Как дела?: ')
    except KeyboardInterrupt:
        return
    while text.strip().capitalize() != 'Хорошо':
        try:
            text = input('Как дела?: ')

        except KeyboardInterrupt:
            print('Пока!')
            break

if __name__ == "__main__":
    hello_user()
