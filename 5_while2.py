"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

answers_dict = {
    'hello': 'greetings professor falken',
    'how are you?': 'fine',
    'what is your name?': 'joshua',
    'get defcon level': '5',
    'get games': 'chess\npoker\nfighter combat\ndesert warfare\n\nglobal thermonuclear war',
    'play a game?': 'let\'s play global thermonuclear war',
    'a nice game of chess?': 'yes, please'
}


exit_request = ['quit', 'exit', 'bye', 'good bye']


def print_wopr_style(msg: str):
    print(msg.upper())


def ask_user(qa_dict):
    print_wopr_style('wopr console')
    while True:
        user_input = input('> ').lower()
        if user_input in qa_dict:
            print_wopr_style(qa_dict[user_input])
        elif user_input in exit_request:
            print_wopr_style('bye-bye')
            break
        else:
            print_wopr_style('i don\'t understand you')


if __name__ == "__main__":
    ask_user(answers_dict)
