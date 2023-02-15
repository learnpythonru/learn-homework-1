"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""


def hello_user():
    user_say = input("Как дела?: ")
    while True:
        try:
            if user_say.capitalize() == "Хорошо":
                print("Вот и хорошо")
                break
            else:
                print("Ну скажи 'Хорошо'?")
                return hello_user()
        except KeyboardInterrupt:
            print("Пока")
            break


if __name__ == "__main__":
    hello_user()

