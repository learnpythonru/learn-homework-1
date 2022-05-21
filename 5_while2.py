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
  'How are you doing?': 'Well',
  'What are you doing?': 'Coding',
  'Are you bored?': 'No',
  'What is your name?': 'Python Bot'
}

def ask_user(answers_dict):
    while True:
        user_inp = input('Ask me anything...\n')
        if user_inp not in questions_and_answers.keys():
            print('Try another question, please.')
            continue
        else:
            print(questions_and_answers[user_inp])
            break


    
if __name__ == "__main__":
    ask_user(questions_and_answers)
