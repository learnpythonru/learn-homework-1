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

questions_and_answers = [{"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Ты молодец?": "Да"}]

def ask_user(answers_dict):
  answers_dict = input("Введите вопрос: ")
  if answers_dict in questions_and_answers:
    print(answers_dict)
  else:
    print("Тогда надо пойти покушать")
#answers_dict    
if __name__ == "__main__":
    ask_user(questions_and_answers)
