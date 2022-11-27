"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    how_are_you = input("Как дела?")
    while how_are_you != "Хорошо":
                return input("Как дела?")
    else:
        pass



if __name__ == '__main__':
    try:
        hello_user()
    except KeyboardInterrupt:
        print('Interrupted')