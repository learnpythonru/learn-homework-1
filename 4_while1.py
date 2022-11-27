"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""
#DONE 


def hello_user():
    how_are_you = input("Как дела?")
    while how_are_you != "Хорошо":
                return input("Как дела?")
    else:
        pass
    
if __name__ == "__main__":
    hello_user()
