"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    question = input("Как дела?: ")
    answer = ("Хорошо")
    if question == answer:
      print("Правильный ответ :)")
    else:
      print("Неправильный ответ, попробуй еще :)")
      return ask_user()
    
if __name__ == "__main__":
    ask_user()
