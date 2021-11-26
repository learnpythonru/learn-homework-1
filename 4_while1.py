"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""


def hello_user():
    while True:
        user_input = input("Как дела?\n").lower().strip()
        if user_input == "хорошо":
            print("Ну, наконец-то! Я уж думал у тебя никогда не хорошо.")
            break

if __name__ == "__main__":
    hello_user()
