"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
  while True:
        hello_user = input('Как дела?: ')
        if hello_user == 'Хорошо':
            return'Это супер!'
            #break
        else:
            print('Нет,', '"', format(hello_user), '"', 'не подходит:(')


    
if __name__ == "__main__":
  check_def = hello_user()
  print(check_def)
