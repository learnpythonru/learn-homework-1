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
    while True:

        try:
            hello = str(input('Как дела чувак? =)'))

            if hello != 'Хорошо':
                print('Я буду задавать вопрос, пока не получу нужный ответ, - "Хорошо"')
                continue
            else:
                print('Рад, что  у тебя все хорошо')
                break

        except KeyboardInterrupt:
            print()
            print('Пока!')
            break
    
if __name__ == "__main__":
    hello_user()
