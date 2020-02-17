"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
question = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую", 'Как погода?': 'Солнечно!'}


def ask_user_dict():
    # не учитываем регистр вопроса
    raw_user_say = input('Введите вопрос: ')
    user_say = raw_user_say.capitalize()
    if user_say in question:
        print(question[user_say])


def ask_user():
    """
    Замените pass на ваш код
    """
    while True:
        try:
            ask_user_dict()
        except KeyboardInterrupt:
            print('Пока!')
            break


if __name__ == "__main__":
    ask_user()
