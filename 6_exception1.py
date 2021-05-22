"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    reply = ''
    while reply.lower() != 'хорошо':
        try:
           reply = input("Как дела?\n")
        except KeyboardInterrupt:
            print('Пока!')
            break
        
if __name__ == "__main__":
    hello_user()
