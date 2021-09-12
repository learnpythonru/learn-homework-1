"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""


def ask_user():
  user_input = input('Как дела?')
  return user_input

def hello_user():
    try:
      ask_user() != 'Хорошо'
            
    except KeyboardInterrupt:
      print('Пока')
          
    
if __name__ == "__main__":
    hello_user()
