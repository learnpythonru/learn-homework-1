"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
import re

regexp = r'\w+'
reg_compiled = re.compile(regexp)


def normalize_answer(answer):
    return reg_compiled.findall(answer.lower())


def hello_user():
    answer = ''
    while 'хорошо' not in normalize_answer(answer):
        try:
            answer = input('Как дела?\n').lower()
        except KeyboardInterrupt:
            print('Пока-пока')
            break


if __name__ == "__main__":
    hello_user()
