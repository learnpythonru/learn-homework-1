"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    """
    Замените pass на ваш код
    """
    
    
    user_message = 0
    while True:
      if user_message == "Хорошо":
        break
      else:
        user_message = input('Как дела? ')
    


    
if __name__ == "__main__":
    ask_user()
