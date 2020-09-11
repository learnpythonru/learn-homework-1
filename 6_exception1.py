"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    x = input('Задайте вопрос: \n')
    qa = {"Как дела?": "Хорошо", \
          "Что делаешь?": "Программирую", \
          "Что изучаешь?": "Python", \
          "Какое сейчас время года?": "Осень"}
    while x in qa:
        try:  
          print(qa[x])
          x = input('Задайте вопрос: \n')
        except KeyboardInterrupt:
            print('Пока!')
            break
    
    
if __name__ == "__main__":
    ask_user()
