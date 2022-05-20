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

questions_and_answers = {"Привет": "Привет", "Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Что пишешь?": "Кода", "А что он делает?": "Ну почти скайнет. Исскучтвенный разум, способный с тобой общаться"}
questions_and_answers_lower = {key.lower(): value for key, value in questions_and_answers.items()}
def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    print("Привет, можешь задать вопрос")
    while True:
      questions = input().lower()
      answer = answers_dict.get(questions)      
      if questions in answers_dict:
        print(answer)
      else:
        print("Не знаю что тебе на это ответить, попробуй ещё раз")
      if questions == "пока":
        print("Пока")
        break

    
if __name__ == "__main__":    
    ask_user(questions_and_answers_lower)
