"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    dictionary = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Как долго?": "Почти целый час"}
    while True:
        try:
            ask_me = input("Спроси у меня? ")
            for key in dictionary:
                if key == ask_me:
                    print(dictionary.get(key))
                    print("Ну, ты это… заходи, если что")
                    return False
            else:
                print("Я не понимаю о чем ты, спроси что нибудь о другом")
                return ask_user()
        except KeyboardInterrupt:
            print("Bye")
            break
        
    
if __name__ == "__main__":
    ask_user()
