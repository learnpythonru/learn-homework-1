"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    while True:
        input_user = input('Как дела?')
        if input_user == 'Хорошо':
            return('Я рад')
        else:
            print('Попробуй еще')
            
print(hello_user())

