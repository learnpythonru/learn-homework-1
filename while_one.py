"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def say_good_to_exit():
    while True:
        if input('Как дела? ') == 'Хорошо':
            break

    
if __name__ == "__main__":
    say_good_to_exit()
