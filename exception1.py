"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

dict1={
    "Как дела?" : "Хорошо",
    "Что делаешь?" : "Программирую"
}

def ask_user():
    """
    Замените pass на ваш код
    """
    while True:
        try:
            message=input('Введите вопрос: ')

            if message in dict1.keys():
                print('Элемент найден!')
                print(dict1[message])
            else:
                print('Элемент не найден!')
        except KeyboardInterrupt:
            print('Пока!')
            break
    
if __name__ == "__main__":
    ask_user()
