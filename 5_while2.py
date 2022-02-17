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
      'Как дела' : 'Хорошо',
      'Что делаешь' : 'Программирую',
      'Где живешь' : 'РФ',
      'Какая школа' : '752',
      'Где работаешь' : 'На фабрике'
}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    question = input('Пользователь: ')
    if question in questions_and_answers:
      print('Программа: ', questions_and_answers(question))
    
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
