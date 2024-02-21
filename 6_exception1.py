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
    whats_up = ""
    while whats_up != "Хорошо":
        try:
            whats_up = input("Как дела? ")
        except(KeyboardInterrupt):
    	    print("Пока!")
    	    break
    	
    
if __name__ == "__main__":
    hello_user()