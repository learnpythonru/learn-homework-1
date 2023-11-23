"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""


def hello_user() -> None:
    """
    Замените pass на ваш код
    """
    answer = None
    while answer != "Хорошо":
        try:
            answer = input("Как дела?\n").strip()
        except KeyboardInterrupt:
            print("\nПока!")
            break
    return


if __name__ == "__main__":
    hello_user()
