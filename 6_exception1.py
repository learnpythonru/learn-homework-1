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
    try:
       while True:
        hay = input('Как дела? ').lower()
        if hay == 'хорошо':
            break 
    except KeyboardInterrupt:
       print('Пока!')
    
if __name__ == "__main__":
    hello_user()
