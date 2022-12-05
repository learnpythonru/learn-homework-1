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
   user_word = input('What does the fox say?')
   if user_word == 'furfur':
     print('oooooooh, so sweet!')
   else:
     print('Am I a joke to you?')
  except KeyboardInterrupt:
    print('Bye!')
    break
    
if __name__ == "__main__":
    hello_user()