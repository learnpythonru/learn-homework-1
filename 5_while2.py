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

questions_and_answers = {"A" : "a", "B" : "b", "C" : "c", "D" : "d"}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    while True:
      answer = input("Введите ваш вопрос, exit - выход\n")
      if answer == 'exit':
        break
      else:
        for key, value in answers_dict.items():
          if key == answer:
            print(value)
    

    
if __name__ == "__main__":
    ask_user(questions_and_answers)
