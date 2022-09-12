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

from pickle import TRUE


questions_and_answers = {
    "Как дела?": "Хорошо!",
    "Что делаешь?": "Программирую.",
    "Какая погода?": "Солнечно.",
}


def ask_user(answers_dict):

    while True:
        question_in = input("Задайте вопрос: ").strip()
        if answers_dict.get(question_in):
            print(answers_dict.get(question_in))
            break
        else:
            print("Я не знаю.")


if __name__ == "__main__":
    ask_user(questions_and_answers)
