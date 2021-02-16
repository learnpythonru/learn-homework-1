"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""
import re

regexp = r'\w+'
reg_compiled = re.compile(regexp)


def normalize_answer(answer):
    return reg_compiled.findall(answer.lower())


def hello_user():
    answer = ''
    while 'хорошо' not in normalize_answer(answer):
        answer = input('Как дела?\n').lower()


if __name__ == "__main__":
    hello_user()
