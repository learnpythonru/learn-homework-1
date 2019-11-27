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
    flag_good = 1
    while flag_good == 1:
        answer_usr = input('Как дела? ')
        if answer_usr == 'Хорошо':
            flag_good = 0

    
if __name__ == "__main__":
    ask_user()
