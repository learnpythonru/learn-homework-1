"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
def hello_user():
    """
    Замените pass на ваш код
    """
    answ = input("How are you? \n")
    try:
        while answ != "Fine":
            print("How are you?")
            answ = input()
    except KeyboardInterrupt:
        print("By")
if __name__ == "__main__":
    hello_user()
