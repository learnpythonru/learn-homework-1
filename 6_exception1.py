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
    question = 'Как дела?'
    while True:
        try:
            user_answer = input(question)
            if user_answer.lower() == "хорошо":
                print('Отлично, верный ответ')
                break
            else:
              question = "Ответ не верный. Как дела?"
        except KeyboardInterrupt:
            print('')
            print('Пока')
            break
   
if __name__ == "__main__":
    hello_user()

