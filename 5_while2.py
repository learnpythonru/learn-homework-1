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
import requests
from pprint import pprint
import requests
from lxml import etree


def get_kurs(valute='Доллар США'):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    root = etree.fromstring(response.content)
    for elem in root.getchildren():
        if elem[3].text == valute:
            current_course = float(elem[4].text.replace(',', '.'))
            break
    return current_course


questions_and_answers = {
    'как дела?': 'Хорошо',
    'что делаешь?': 'Ничего',
    'курс доллара?': get_kurs(),
    'nothing': 'Не понял вопроса',
    'курс фунта?': get_kurs('Фунт стерлингов Соединенного королевства'),
    'какая погода завтра?': "Здесь мог бы быть прогноз, но с вероятностью > 90% погода на завтра бывает такой же как сегодня :-)",
}


def ask_user(answers_dict):
    while True:
        question = input('Введите вопрос:\n')
        if '?' not in question:
            question = question + '?'

        answer = questions_and_answers.get(question.lower(), "Не понял вопроса")
        print(answer)


if __name__ == "__main__":
    ask_user(questions_and_answers)