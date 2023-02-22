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



def ask_user():
    """
    Замените pass на ваш код
    """

    questions_and_answers = {"как дела?": "Хорошо!", "что делаешь?": "Программирую", "как погода?": "Солнечно!",
                             "что по настроению?": "Отличное",
                             "как проходит обучение?": "не без трудностей, но я справлюсь!",
                             "выход?": "Пока пока"}
    vopros = 'Задайте вопрос: '
    while True:
        user_answer = input(vopros).lower()
        if user_answer in questions_and_answers:
            print(questions_and_answers[user_answer])
            """Выход по ввводу этой фразы"""
            if user_answer == "выход?":
                break
        else:
            print('вопроса нет в перечне, или Вы забыли добавить знак вопроса')


if __name__ == "__main__":
    ask_user()
