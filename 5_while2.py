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
            "How are you?": "Thanks, I'm fine :)",
            "Where are you from?": "I'm from Siberia!",
            "How old are you?": "I'm 28 years old",
            "What are you doing?": "I'm coding :)",
            "Where are you?": "I'm in a business trip",
            }

def ask_user(self):
    while True:
        user_answer = input("Enter your question, please ")
        if user_answer in questions_and_answers:
            print(questions_and_answers[user_answer])
        else:
            print("Good bye!")
            break

ask_user(questions_and_answers)
