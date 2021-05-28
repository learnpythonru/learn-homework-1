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

questions_and_answers = {
    'Hello': 'Hello',
    'How are you?': 'I am good, thanks',
    'What are doing?': 'I am learning Python',
    'Do you like it?': 'Yes, it is interesting',
    'How long do you study Python?': 'It is been few weeks already',
    'Okay, bye!': 'Bye!'
}

def ask_user(answers_dict):
    answers_dict = input()
    for question, answer in questions_and_answers.items():
        while answers_dict == question:
            print(answer)
            break
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
