"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    dict = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}


    try:
        while True:
                user_ask = input('Задайте вопрос: ')
                if user_ask == "Как дела":
                    print(dict["Как дела"])
                elif user_ask == "Что делаешь?":
                    print(dict["Что делаешь?"])
    except(KeyboardInterrupt):
        print("Пока")
    # зачем тут завершение через break ?

if __name__ == "__main__":
    ask_user()
