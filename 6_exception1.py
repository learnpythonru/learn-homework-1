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
            user_input = input('How are you?\n')
            if user_input == 'Good':
                break
        except KeyboardInterrupt:
            print('Goodbye')
            break  

if __name__ == "__main__":
    hello_user()
