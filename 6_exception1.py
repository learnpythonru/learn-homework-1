"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
  while True:
      try:
        hello_user = input('Как дела?: ')
      except KeyboardInterrupt:
          print('Пока')
      if hello_user == 'Хорошо':
          return'Это супер!'
      else:
          print('Нет,', '"', format(hello_user), '"', 'не подходит:(')

    
if __name__ == "__main__":
  check_def = hello_user()
  print(check_def)
