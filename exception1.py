"""
Домашнее задание №1
Исключения: KeyboardInterrupt
* Перепишите функцию ask_user() из задания while2, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""

ask_answer = {'How are u': 'Ok!',
              'What are u doing':'Programming',
              'How old are u': 'Im 30',
              'Where are u from?': 'From Penza City'}


def ask_user():

    while True:
        try:
            point_break = input('Ask your question or input "exit" for exit: > ')

            for key in ask_answer:
                if point_break == key:
                    answer = ask_answer[key]
                    print(answer)
        except KeyboardInterrupt:
            print('Пока!')
            break


if __name__ == "__main__":
    ask_user()