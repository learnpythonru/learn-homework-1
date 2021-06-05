import logging
import ephem
import numexpr as ne
from random import randint
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date, datetime
from settings import TOKEN, PROXY

"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

date_now = date.today()


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def in_which_constellation(update, context):
    user_text = update.message.text.split()[1].capitalize()
    planet = getattr(ephem, user_text)
    constellation = ephem.constellation(planet(date_now))[1]
    update.message.reply_text(f'Планета {user_text} в созвездии {constellation}')


# Следующее полнолуние
def next_full_moon(update, context):
    try:
        user_text = update.message.text.split()[1]
        user_date = datetime.strptime(user_text, '%Y-%m-%d')
        update.message.reply_text(f'Следующее полнолуние {ephem.next_full_moon(user_date)}')
    except IndexError:
        update.message.reply_text(f'Следующее полнолуние {ephem.next_full_moon(date_now)}')


# Калькулятор
def calculate(update, context):
    user_text = update.message.text.split(' ')
    str_expr = ''.join(user_text[1:])
    try:
        result = ne.evaluate(str_expr)
    except ZeroDivisionError:
        update.message.reply_text('Нельзя делить на ноль')
    update.message.reply_text(f'{result}')


def helper(update, context):
    update.message.reply_text('Команда /planet работает следующим образом\nНапример: /planet Jupiter\n'
                              'А так же: \nMars,\nMercury,\nMoon,\nNeptune, Pluto,'
                              '\nSaturn, Uranus, Venus, Jupiter')


def create_cities_list():
    with open('goroda.csv', 'r', encoding='utf-8') as f:
        li = []
        for i in f:
            li.append(i.split(',')[0])
        return li


players = {}


def cities_game(update, user_data):
    """
    Основная часть игры в города.
    """
    global players
    user_id = user_data.get('user_id')
    user_city = user_data.get('text')
    last_letter = players.get(user_id)['last_letter']
    if user_city.lower() == 'stop':
        players.pop(user_id)
        update.message.reply_text('Игра окончена!')
    elif (user_city in players.get(user_id).get('cities_list') and user_city[0] == last_letter) or last_letter == '0':
        players.get(user_id)['last_letter'] = get_last_letter(user_city).upper()
        players.get(user_id).get('cities_list').remove(user_data.get('text'))
        temp_list_cities = []
        for city in players.get(user_id)['cities_list']:
            if city[0] == players.get(user_id)['last_letter']:
                temp_list_cities.append(city)
        bot_city = temp_list_cities[randint(0, len(temp_list_cities))]
        players.get(user_id)['last_letter'] = get_last_letter(bot_city).upper()
        update.message.reply_text(bot_city)
        update.message.reply_text(f'Тебе на "{players.get(user_id)["last_letter"]}"')
        players.get(user_id).get('cities_list').remove(bot_city)
    else:
        update.message.reply_text(f'Не не, тебе на "{players.get(user_id)["last_letter"]}"')


def check_players(user_data):
    """
    Проверяем наличие пользователя в списке игроков, если в списке его нет, добавляем.
    """
    global players
    if user_data.get('user_id') not in players:
        players[user_data.get('user_id')] = {'city': user_data.get('text'),
                                             'last_letter': '0', 'cities_list': create_cities_list()}


def get_last_letter(word):
    """
    Получаем последнюю букву города
    """
    if word[-1] == 'й':
        result = 'и'
    elif word[-1] in ['ь', 'ы']:
        result = word[-2]
    else:
        result = word[-1]
    return result


# Города
def cities(update, context):
    """
     По команде /cities <Название города> начинается игра с ботом в "Города"
    """
    global players
    user_data = {'user_id': update.message.chat.id, 'text': context.args[0].capitalize()}
    check_players(user_data)
    cities_game(update, user_data)


def wordcount(update, context):
    user_text = update.message.text.split(' ')[1:]
    print(user_text)
    if not user_text:
        update.message.reply_text('это что такое? пустая строка? и что прикажешь считать?')
    else:
        update.message.reply_text(f'{len(user_text)} слова')
# /wordcount 1234567 2345678 @#$%ˆ&*  - подумать как сделать проверку


def main():
    mybot = Updater(TOKEN, request_kwargs=PROXY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", in_which_constellation))
    dp.add_handler(CommandHandler("help", helper))
    dp.add_handler(CommandHandler('wordcount', wordcount))
    dp.add_handler(CommandHandler('next_full_moon', next_full_moon))
    dp.add_handler(CommandHandler('cities', cities))
    dp.add_handler(CommandHandler('calc', calculate))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
