"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""

def hello_user():
    def hello_user():
        return input('Как дела ? \n')

    while True:
        if hello_user() != 'Хорошо':
            continue
        else:
            break
    
if __name__ == "__main__":
    hello_user()
