"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    try:
        n = input('Как дела?').strip().capitalize()
        while n != 'Хорошо':
            n = input('Как дела?').strip().capitalize()
        else:
            print('И это хорошо!')

    except KeyboardInterrupt:
        print()
        print('Пока!')
          
if __name__ == "__main__":
    hello_user()
