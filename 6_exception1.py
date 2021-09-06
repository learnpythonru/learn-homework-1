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
            input_user = input('Как дела?')
            if input_user == 'Хорошо':
                return('Я рад')
            else:
                print('Попробуй еще')
        
        except KeyboardInterrupt:
            print('Пока!')
            break



if __name__ == "__main__":
    print(hello_user())
