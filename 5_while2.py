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

questions_and_answers = {"How are you?": "Fine", 
                         "What are you doing?": "I'm programming",
                         "What are you doing tonight?": "Watching TV serie"
}

def ask_user(answers_dict):
    ask_question = input("Ask me something \n")
    if ask_question in answers_dict: 
        print(questions_and_answers[ask_question])
    else:
        print("I don't understand, try again")
        ask_user(questions_and_answers)

    
if __name__ == "__main__":
    ask_user(questions_and_answers)
