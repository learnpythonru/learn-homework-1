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
    
    answer_dict = {'Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую',
                'Ты голоден?': 'Есть немного :)', 'Как погода в Москве?': 'Мерзкая'}
    answer_usr = input("Для начала разговора введите вопрос: ")
    while answer_usr:
        try:
            print(answer_dict[answer_usr])
            answer_usr = input("Ещё вопросик!? ")
        except(KeyError):
            answer_usr = input("Может другой вопрос? ")
        except(KeyboardInterrupt):
            print('\nПока!')
            break 
        
if __name__ == "__main__":
    ask_user()
