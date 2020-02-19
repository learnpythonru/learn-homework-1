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
    question_answer = {'Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую', 'Какая сегодня погода?': 'Хорошая'}
    while True:
        try:
            user_says = input('Введите вопрос ')
            if user_says in question_answer:
                print(question_answer[user_says])
        except KeyboardInterrupt:
            print('Пока!')
            break
    
if __name__ == "__main__":
    ask_user()
