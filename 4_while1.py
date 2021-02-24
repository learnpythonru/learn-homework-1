"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""

def hello_user():
    user_say = input('Как дела? ')
   
    while user_say != 'Хорошо':
        user_say = input('Так всё таки, как дела? ')
    return user_say
    
if __name__ == "__main__":
    hello_user()
