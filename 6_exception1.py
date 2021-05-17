"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    s = input('Как дела? ')
    
    while s != 'Хорошо':
        try:
            s = input('Как дела? ')
        except KeyboardInterrupt:
            print('\n', 'Пока', sep='')
            break
        
        


if __name__ == "__main__":
    hello_user()
