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
    while True:
        how_are_you = input('Как дела ? ')
        if how_are_you == 'Хорошо':
            print('Ну и хорошо')
            break
        else:
           how_are_you
        
    
if __name__ == "__main__":
    ask_user()
