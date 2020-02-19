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
    answer = input('Как твои дела? ')
    while answer != "Хорошо":
        return ask_user()
    else:
        print("Хорошо что хорошо")



    
if __name__ == "__main__":
    ask_user()
