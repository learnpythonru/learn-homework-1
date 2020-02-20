"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

phrases = {"Как дела?":"Отлично!",
           "Что делаешь?":"Решаю задачи по python",
           "Что нового?":"Записался на курс по python",
           "Сколько тебе лет?":"32",
           "Привет!":"Салют!"}


def ask_user():
    """
    Замените pass на ваш код
    """
    while True:
        try:
            ask_question = input("Задай вопрос: ")
            for n in phrases:
                    if n == ask_question:
                        print(phrases.get(ask_question))
        except KeyboardInterrupt:
            print("Пока!")
            break


if __name__ == "__main__":
    ask_user()
