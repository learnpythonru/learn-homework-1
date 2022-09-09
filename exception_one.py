"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""



def say_good_to_exit():
    answer = ''
    while answer != 'Хорошо':
        try:
            answer = input('Как дела? ')
        except KeyboardInterrupt:
            print('Пока!')
            break


if __name__ == "__main__":
    say_good_to_exit()
