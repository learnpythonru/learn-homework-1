"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""


def hello_user():
    """
    почему то не работает :-(
    не реагирует на ctrl+c и на delete не реагирует

    """

    answer = ''
    while answer != 'хорошо':
        try:
            answer = input('Как дела?\n').lower()
            answer = float(answer)
        except Exception as exp:
            # этот вот работает если ввести строку например
            print(exp)
            break
        except KeyboardInterrupt as exp:
            # а вот этот не ловится. не могу понять почему?
            print(exp)
            break



if __name__ == "__main__":
    hello_user()
