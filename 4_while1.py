"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    """
    Замените pass на ваш код
    """
    question = 'Как дела?'
    while True:
          user_answer = input(question)
          if user_answer.lower() == "хорошо":
                print('Отлично, верный ответ')
                break
          else:
                question = "Ответ не верный. Как дела?"
   
if __name__ == "__main__":
    hello_user()
