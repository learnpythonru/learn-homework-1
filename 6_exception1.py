"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    flag = True
    while flag:
      try:
          command = input("Как дела? ")
          if command.lower() == "хорошо":
              flag = False
      except KeyboardInterrupt:
        print("\nПока!")
        break

    
if __name__ == "__main__":
    hello_user()
