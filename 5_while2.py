"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""
from datetime import datetime


questions_and_answers = {'привет': 'Прифки, как дела?',
                         'хорошо': 'Ну и отлично!',
                         'что делаешь?': 'Общаюсь с тобой)',
                         'расскажи анекдот': '-Knock-knock, -Who is there?, -Police!, -Police, who?,-There is cold. '
                                             'Please open up!',
                         'скажи время?': datetime.now()}


def ask_user(answers_dict):
    question = str(input("Привет, введи вопрос? "))
    for que, ans in answers_dict.items():
         if que == question:
            return ans


if __name__ == "__main__":
    ask_user(questions_and_answers)
