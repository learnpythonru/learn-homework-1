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
    answers = {
        'Как дела?': 'Восхитительно!',
        'Что делаешь?': 'Прокрастинирую',
        'Как тебя зовут?': 'Антошка'
    }

    try:
        while True:
            question = input("Спроси меня\n")
            for answer in answers:
                if answer == question:
                    print(answers[question])
    except KeyboardInterrupt:
        print("\nПока!")

if __name__ == "__main__":
    ask_user()
