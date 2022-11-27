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
#NEED TO THINK MORE NOTHING HELPS 
#HOW TO LOOP THROUGH DICT AND GET THE VALUE 

questions_and_answers = {
    "question": "Что делаешь?",
    "answer":"Программирую"
}

def ask_user(answers_dict):
  user_question = input("Спроси меня, что я делаю:\n")

  for i in questions_and_answers:
        while user_question == questions_and_answers[i]:
            return questions_and_answers["answer"]
        else:
            return "Я вас не понимаю, запустите программу ещё раз и спросите что я делаю."

    
if __name__ == "__main__":
    print(ask_user(questions_and_answers))
