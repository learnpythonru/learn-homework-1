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
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config
import time
import ephem

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}

current_game_known_cities = ['Москва', 'Альметьевск', 'Киров', 'Волгоград', 'Дзержинск']

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)

def wordcount(update, context):
    user_text = update.message.text
    print(user_text)
    user_text = user_text.strip('/wordcount ').split()
    text = f'{len(user_text)} слова'
    if len(user_text) == 0:
        text = 'Нет ни слов, ни чисел даже'
        print(text)

    update.message.reply_text(text)

def where_is_planet(update, context):
    today = time.strftime('%Y/%m/%d')
    user_text = update.message.text
    print(user_text)
    planet = (user_text.split()[1])
    update.message.reply_text(user_text.split()[1])
    if planet in ['Mars', 'Jupiter', 'Mercury', 'Pluto']:
        if planet == 'Mars': planet = ephem.Mars(today)
        elif planet == 'Jupiter': planet = ephem.Jupiter(today)
        elif planet == 'Mercury': planet = ephem.Mercury(today)
        elif planet == 'Pluto': planet = ephem.Pluto(today)
        constellation = ephem.constellation(planet)
        print(constellation)
        update.message.reply_text(constellation)

def next_full_moon(update, context):
    user_text = update.message.text
    print(user_text)
    today = (user_text.split()[1])
    full_moon_date = ephem.next_full_moon(today)
    full_moon_date = ephem.date(full_moon_date + ephem.hour)
    print(full_moon_date)
    update.message.reply_text(f'Дата и время следующего полнолуния: {full_moon_date}')

def game_cities(update, context):
    #known_cities = ['Москва', 'Альметьевск', 'Киров', 'Волгоград', 'Дзержинск']
    #current_game_known_cities = ['Москва', 'Альметьевск', 'Киров', 'Волгоград', 'Дзержинск']
    current_game_called_cities = []
    user_text = update.message.text

    city = user_text.split()[1]
    print(city)

    if city in current_game_called_cities:
        return update.message.reply_text(f'Баян, уже было')

    current_game_known_cities.remove(city)
    current_game_called_cities.append(city)

    for answer_city in current_game_known_cities:
        if answer_city[0].lower() == city[-1].lower():
            update.message.reply_text(f'{answer_city}. Твой ход')
        update.message.reply_text(f'Больше не знаю городов на {city[-1]}. Надо бы узнать. Пиши /cities Заново и начнём сначала. ')

    if current_game_known_cities == []:
        update.message.reply_text(f'Мы больше не знаем никаких городов. Напиши город Заново и начнём сначала')

    if user_text.split()[1] == 'Заново':
        return update.message.reply_text(f'Начинаем заново')

def calc(update, context):
    user_text = update.message.text
    user_text = (user_text.split()[1])
    print(user_text)
    if user_text[1] == '+':
        result = int(user_text[0]) + int(user_text[2])
        update.message.reply_text(result)
    elif user_text[1] == '-':
        result = int(user_text[0]) - int(user_text[2])
        update.message.reply_text(result)
    elif user_text[1] == '*':
        result = int(user_text[0]) * int(user_text[2])
        update.message.reply_text(result)
    elif user_text[1] == '/':
        result = int(user_text[0]) / int(user_text[2])
        update.message.reply_text(result)


def main():
    #mybot = Updater(config.TOKEN, request_kwargs=PROXY, use_context=True)
    mybot = Updater(config.TOKEN, use_context=True)
    dp = mybot.dispatcher

    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('planet', where_is_planet))
    dp.add_handler(CommandHandler('next_full_moon', next_full_moon))
    dp.add_handler(CommandHandler('cities', game_cities))
    dp.add_handler(CommandHandler('wordcount', wordcount))
    dp.add_handler(CommandHandler('calc', calc))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()