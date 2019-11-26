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
import datetime

def ask_user_dict():
    phrase_map_dict ={"how's it going?": 'good!', 
    'hi':'Hello!',
    'yes': 'no',
    'no': 'yes',
    'python': 'Oo you are understand me, friend',
    'what are you doing?': "I'm programming", 
    'what time is it?': datetime.datetime.now().strftime('time ~ %H:%M:%S\ndate ~ %d %B %Y'),
    'what the power is?': 'Python:)'
    }
    
    while True:
        user_text =  input('-You wanna to say something?-\n').lower()

        if user_text == 'power off':
            print('See you later')
            break
        user_text = phrase_map_dict.get(user_text, "I don't even know what to tell you.")

        print(f'{len(user_text)*"~"}\n{user_text}\n{len(user_text)*"~"}\n')
   
if __name__ == "__main__":
    ask_user_dict()
