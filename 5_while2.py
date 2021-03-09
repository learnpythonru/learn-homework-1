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
  'Как дела?': 'Нормально',
  'Что делаешь?': 'Работаю',
  'Какая погода?': 'Снежная',
  'Какие планы на завтра?': 'Выспаться',
}
# Первый вариант через keys
# def ask_user(answers_dict):
#     while True: 
#         user_question = input('Задай свой вопрос: ')
#         if user_question in answers_dict.keys():
#             print(answers_dict[user_question])
#         else:
#             print('Затрудняюсь ответить.')

# Второй вариант через get
def ask_user(answers_dict):
    while True: 
        user_question = input('Задай свой вопрос: ')
        if questions_and_answers.get(user_question):
            print(answers_dict[user_question])
            
        else: 
            print(questions_and_answers.get(user_question, 'Затрудняюсь ответить'))

    
if __name__ == "__main__":
    ask_user(questions_and_answers)
