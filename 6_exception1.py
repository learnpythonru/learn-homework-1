"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""


def ask_user():
    answer_dict = {
        'Как дела?': 'Хорошо',
        'Что делаешь?': 'Программирую',
        'Как погода?': 'Солнечно',
        'Что программируешь?': 'Дз по Python',
    }
    while True:
        try:
            answer = input('Введите сообщение: ')
        except KeyboardInterrupt:
            print('\nПока!')
            break
        try:
            return answer_dict[answer]
        except KeyError:
            continue


if __name__ == "__main__":
    ask_user()
