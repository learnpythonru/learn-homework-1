"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break
"""

PHRASES = {
    "привет!": "привет!",
    "как дела?": "хорошо!",
    "что делаешь?": "программирую",
    "пошли гулять!": "некогда!",
    "а где бабуля?": "я за неё"
}


def ask_user():
    while True:
        try:
            question = input("Ваш вопрос: ").strip().lower()
        except KeyboardInterrupt:
            print("Пока!")
            break
        print(PHRASES.get(question, default="Что?").capitalize())


if __name__ == "__main__":
    ask_user()
