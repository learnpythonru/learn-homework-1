"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
        
    while True:
        check_status = input("Как дела? ")
        if check_status == "Хорошо":
            print("Отлично!")
            break
        else:
            print("Тогда надо пойти покушать")
        
  
if __name__ == "__main__":
    hello_user()
