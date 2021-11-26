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


questions_and_answers = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", 'А давно?': 'Уже минут 50', 'Нравится?': 'Ну конечно'}


def ask_user(questions_and_answers):
    """
    Замените pass на ваш код
    """
    run = True
    while run == True:
        question = input('Введите вопрос: ')
        result = questions_and_answers.get(question)
        if result != None:
            print(result)
        elif question == 'Ладно пока':
            return 'Ну пока'
        else:
            print('Введите другой вопрос')


if __name__ == "__main__":
    action = ask_user(questions_and_answers)
    print(action)
