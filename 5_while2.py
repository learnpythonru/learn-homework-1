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

questions_and_answers = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую", "Сколько звезд на небе?": "Почем мне занть!"}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    ques = ''
    while ques != 'exit':
      ques = input('Введите ваш вопрос! ')
      answer = answers_dict.get(ques)
      if answer:
        print(answer)
      elif ques == 'exit':
        break
      else:
        print('Спроси чтонибудь еще!(Введи "exit", для выхода)')





if __name__ == "__main__":
    ask_user(questions_and_answers)
