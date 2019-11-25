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
    while True:
        try:
            how_are_you = input('Как дела ? ')
            if how_are_you == 'Хорошо':
                print('Ну и хорошо')
                break
            else:
                how_are_you
        except KeyboardInterrupt:
            print('\nПока !')
            break
    
if __name__ == "__main__":
    ask_user()
