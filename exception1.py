"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
import datetime

def ask_user():
    phrase_map_dict ={'how\'s it going?': 'good!', 
    'hi':'Hello!',
    'yes': 'no',
    'no': 'yes',
    'python': 'Oo you are understand me, friend',
    'what are you doing?': 'I\'m programming', 
    'what time is it?': datetime.datetime.now().strftime('time ~ %H:%M:%S\ndate ~ %d %B %Y'),
    'what the power is?': 'Python:)'
    }
    
    try:
        while True:
            user_text =  input('-You wanna to say something?-\n').lower()

            if user_text == 'power off':
                print('See you later')
                break
            user_text = phrase_map_dict.get(user_text, 'I don\'t even know what to tell you.')

            print(f'{len(user_text)*"~"}\n{user_text}\n{len(user_text)*"~"}\n')
    except KeyboardInterrupt:
        print('\nGood bye!')
    
if __name__ == "__main__":
    ask_user()
