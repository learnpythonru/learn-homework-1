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
    while True:
      try:
        answer = input("Как дела? ")
        if answer == "Хорошо":
          break
      except KeyboardInterrupt:
        print("\nПока!")
        break
    
if __name__ == "__main__":
    hello_user()
