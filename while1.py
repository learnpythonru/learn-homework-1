"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""

def ask_user():
    try_text = 'How are you?\nTell me: '
    
    while input(f'{try_text}\n') != 'Good':
        try_text = 'Wrong answer, try again: '
        
    print('You are finally doing well!)')
 
if __name__ == "__main__":
    ask_user()
