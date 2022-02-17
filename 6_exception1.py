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
some = True
while some:
   
    user_say = input('Как дела?: ')
    if user_say == 'Хорошо':
        print('Договорились!')
    else:
        print('Твой ответ: {}'.format(user_say), '- не подходит')
    try:
        user_say = input('Прощаемся?: ')
        some = {}.get(user_say)
        user_say2 = some if some else 'Пока!'
        print(user_say2)    
    except KeyboardInterrupt:
          break

if __name__ == "__main__":
    hello_user()
