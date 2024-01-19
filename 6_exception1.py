"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
  try:
    while True:
        check_status = input("Как дела? ")
        if check_status == "Хорошо":
          print("Отлично!")
          break
        else:
          print("Для остановки программы нажмите Ctrl+C")
          
  except KeyboardInterrupt:
    print('Пока!')

    
if __name__ == "__main__":
    hello_user()