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

    while True:
        user_say = input('Как дела? ')
        if user_say != 'Хорошо':
          continue
        else:
          break

    

    
if __name__ == "__main__":
    hello_user()
