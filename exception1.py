"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
question_answer = {"Как дела": "Хорошо!", "Что делаешь": "Программирую", "Как погода": "Жара!", "Как работа": "Как всегда!"}

def ask_user():
    while True:
        try:
            question = input('Задай вопрос: ')
            if question in question_answer: 
                print(question_answer[question])
        except KeyboardInterrupt:
            print('  Пока')
            break
if __name__ == "__main__":
    ask_user()
