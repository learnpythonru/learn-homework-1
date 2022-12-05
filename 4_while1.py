"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    while True:
        user_word = input('What does the fox say?')
        if user_word == 'furfur':
            print('oooooooh, so sweet!')
            break
        else:
            print('Am I a joke to you?')

    
if __name__ == "__main__":
    hello_user()
