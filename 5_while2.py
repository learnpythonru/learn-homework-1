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

questions_and_answers = {"How are you":'Good',"What are you doing":"I am programming"}

def ask_user(answers_dict):
    while True:
        user_input = input('Enter a question:\n')
        if user_input in answers_dict:
            print(questions_and_answers[user_input])
        if user_input in answers_dict:
            break
if __name__ == "__main__":
    ask_user(questions_and_answers)
