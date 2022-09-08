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



def ask_user(answers_dict):
    question = ''
    while question != 'Выход':
        question = input('Задайте вопрос: ')
        if question != 'Выход':
            print(questions_and_answers.get(question))
            if question not in questions_and_answers.keys():
                print(f'Я понимаю только следующие вопросы: {questions_and_answers.keys()}')

if __name__ == "__main__":
    questions_and_answers = {
    'Привет': ':)', 'Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую', 'Сколько будет 2+2?': '4'
    }
    ask_user(questions_and_answers)
