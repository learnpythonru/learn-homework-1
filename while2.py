"""
Домашнее задание №1
Цикл while: ask_user со словарём
* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит
  пользователя ввести вопрос, а затем, если вопрос есть в словаре,
  программа давала ему соотвествующий ответ. Например:
    Пользователь: Что делаешь?
    Программа: Программирую

"""
ask_answer = {'How are u': 'Ok!',
              'What are u doing': 'Programming',
              'How old are u': 'Im 30',
              'Where are u from?': 'From Penza City'}


def ask_user():
    point_break = ''

    while point_break != 'exit':
        point_break = input('Ask your question or input "exit" for exit: > ')
        if point_break == 'exit':
            break
        try:
            print(ask_answer[point_break])
        except:
            print('Неверный вопрос')


if __name__ == "__main__":
    ask_user()
