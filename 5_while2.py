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

questions_and_answers = {'How are you?': 'How are you', 
                         'How old are you?': 'Next question :)', 
                         'Do you like cats?': 'Im obsessed with this sweet fury creatures'
}

def ask_user(questions_and_answers):
  while True:
    start = input('Ask a question: ')
    answer = questions_and_answers.get(start, "wtf")
    print(answer)
    

ask_user(questions_and_answers)