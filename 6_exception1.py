"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""


def hello_user():
    return input('Как дела ? \n')

while True:
    if hello_user() != 'Хорошо':
        continue
    else:
        break
    
if __name__ == "__main__":
    hello_user()
