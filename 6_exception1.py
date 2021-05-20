"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user3():
    while input('Как дела? ') != 'Хорошо':
        pass
    print('Рад за Вас')


if __name__ == "__main__":
    try:
        hello_user3()
    except KeyboardInterrupt:
        print('\nПока!')
