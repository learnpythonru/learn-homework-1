"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
NO_ANSW_CODE = 0

GREET_MSG = 'Привет!'
NO_ANSW_MSG = 'Не знаю :\'('

def ask_user():
    default_dict = {
        "как дела": "Прекрасно!",
        "что делаешь": "Исправно работаю",
        "может, сходим куда-нибудь": "Извини, сегодня не могу...",
        "в чём смысл жизни": "42",
    }
    print(GREET_MSG)
    while True:
        try:
            query = input('Пользователь: ').lower().replace('?', ' ').strip()
        except KeyboardInterrupt:
            print('Пока!')
            break
        response = default_dict.get(query, NO_ANSW_CODE)
        if response == NO_ANSW_CODE:
            print('Программа: ' + NO_ANSW_MSG)
        else:
            print('Программа: ' + response)
    
if __name__ == "__main__":
    ask_user()
