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

questions_and_answers = {'question_1': 'Как дела?', 'question_2': 'Что делаешь?', 'question_3': 'Все получается?',
'answer_1': 'Хорошо', 'answer_2': 'Программирую', 'answer_3': 'Могло быть и лучше :('
 }

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
while True:
    ask_user = input('Задайте вопрос: ' )
    if ask_user == questions_and_answers['question_1']:
        print(questions_and_answers['answer_1'])
    elif ask_user == questions_and_answers['question_2']:
        print(questions_and_answers['answer_2'])
    elif ask_user == questions_and_answers['question_3']:
        print(questions_and_answers['answer_3'])    
    else:
      try:
        print('Данного вопроса: {}'.format(ask_user), '- в словаре нет :( попробуй что-нибудь еще :)')
      except TypeError:    
        break
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
