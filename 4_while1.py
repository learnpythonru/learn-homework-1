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
    whats_up = input("Как дела? ")
    while whats_up != "Хорошо":
    	whats_up = input("Как дела? ")
#whats_up = 0    
#while whats_up == "Хорошо":
  #  hello_user()

    
if __name__ == "__main__":
    hello_user()
