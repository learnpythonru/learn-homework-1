"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    questions = {"Как тебя зовут?": "Борис", "Сколько тебе лет?": "30", "Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}
    
      
    def ask_user_dict():
      while True:
        try:
          user_message = input('Спроси меня что-нибудь ')
          for i in questions: 
            if user_message == i:
              print(questions[i])
        except KeyboardInterrupt:
          print("")
          print("Пока!")
          break
      
            
    ask_user_dict()
    
if __name__ == "__main__":
    ask_user()
