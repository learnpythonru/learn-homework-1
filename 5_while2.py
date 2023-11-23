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

questions_and_answers = {"как дела?": "Хорошо!", "что делаешь?": "Программирую"}


def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    num_questions = len(answers_dict)
    print(f'У вас есть {num_questions} попыток задать вопрос')
    while num_questions:
        question = input('Задайте вопрос роботу:\n').strip().lower()
        answer = answers_dict.get(question, '')
        print(answer)
        num_questions -= 1


if __name__ == "__main__":
    ask_user(questions_and_answers)
