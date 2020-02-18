"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

dict_faq = {"Как дела": "Хорошо!",
        "Что делаешь?": "Программирую",
                  "ЯП": "PYTHON!",
             "Ты кто?": "Skynet",
           "Арни, ты?": "Нет, это другой Т101",
               "Пора?": "Да",
        }

def ask_user_dict(quest):
    return dict_faq.get(quest, None)


def ask_user():
    """
    Замените pass на ваш код
    """
    while True:
        try:
            answer = ask_user_dict(input('Пользователь: '))
            if answer is None:
                break
            else:
                print('Программа: {}'.format(answer))
        except KeyboardInterrupt:
            print("\nПока!")
            break
    
if __name__ == "__main__":
    ask_user()
