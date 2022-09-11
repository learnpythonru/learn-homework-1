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
            answer = input('Как дела? \n').capitalize()   # сделает первую введенную букву заглавной
            if answer == 'Хорошо':
                break
        except KeyboardInterrupt:
            print('Пока!')
            break

if __name__ == "__main__":
    hello_user()
