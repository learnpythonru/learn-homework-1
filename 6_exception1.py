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
      while True:
        user_say = input('Как дела? ')
        if user_say.lower() == 'хорошо':
            print('Ну отлично! Пока.')
            break
    except KeyboardInterrupt:
       print()  # Чтобы сообщение 'Пока!' выдавалось на след строке
       print('Пока!')

if __name__ == "__main__":
    hello_user()
