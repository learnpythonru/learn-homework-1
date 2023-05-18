import random

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
import time

questions_and_answers = {'как дела': ('Отлично!!!', 'Хорошо)', 'Так себе('), 'кто ты': ('ИИ', 'Не знаю', 'Программа'),
                         'что делаешь': ('Программирую', 'Ничего', 'Секрет'),
                         'как тебя зовут': ('У меня много имен', 'Секрет')}


def ask_user(answers_dict):
    while True:
        time.sleep(0.7)
        question = input('Введите вопрос:\nUser: ').strip().lower()
        if question in questions_and_answers:
            print(f'AI: {random.choice(questions_and_answers[question])}')
        elif question.lower() in ['хватит', 'стоп', 'stop']:
            break
        else:
            time.sleep(0.7)
            print('Такого вопроса нет в общей базе')
            time.sleep(1)
            print('Придумайте свой ответ на этот вопрос')
            time.sleep(1)
            questions_and_answers[question] = (input('Введите ответ на вопрос:\nUser: '.strip()),)


if __name__ == "__main__":
    ask_user(questions_and_answers)
