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
    questions_and_answers = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}
    while True:
        try:
            a = input()
            if a in questions_and_answers:
                print(questions_and_answers[a])
            else:
                print('Такого вопроса нет')
        except KeyboardInterrupt:
            print('Пока!')
            break
    
if __name__ == "__main__":
    hello_user()
