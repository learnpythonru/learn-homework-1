import urllib.request
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
def external_ip():
    external_ip = str(urllib.request.urlopen('https://ident.me').read().decode('utf8')) #Обработать try/except
    return external_ip
ext_ip = external_ip()
questions_and_answers = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Какой у тебя ip?": f'{ext_ip}'}
quest = ''.join(f'{k}'+',' for k in questions_and_answers.keys())

def ask_user(answers_dict):
    q = f'Возможные вопросы:\n{quest}'
    print(q)
    while True:
        try:
            questions = (input('Введите вопрос:')).lower()
            a = questions_and_answers.get(questions.capitalize())
            if a:
                print(a)
            else:
                print(f'----Введите вопрос из списка!----\n{q}\nЧтобы выйти, нажмите Ctrl+C')
                continue
        except KeyboardInterrupt:
            break
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
