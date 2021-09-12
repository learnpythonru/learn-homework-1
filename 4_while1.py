"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""

def ask_user():
  user_input = input('Как дела?')
  return user_input

def hello_user():
    while ask_user() != 'Хорошо':
      ask_user()

if __name__ == "__main__":
    hello_user()
