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
    user_say = None
    try:
        while user_say != 'Хорошо': #Выполнять цикл пока user_say не станет 'Хорошо'
            user_say = input('Как дела?\n') #\n переход на следующую строку
    except KeyboardInterrupt:
            print('Пока')

if __name__ == "__main__":
    hello_user()
