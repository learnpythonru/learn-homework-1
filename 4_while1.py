"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    n = input('Как дела?').strip().capitalize()
    while n != 'Хорошо':
        n = input('Как дела?').strip().capitalize()
    else:
        print('И это хорошо!')

    
if __name__ == "__main__":
    hello_user()
