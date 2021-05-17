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
import ephem
import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

load_dotenv()

PROXY = {
    'proxy_url': os.getenv('PROXY_URL'),
    'urllib3_proxy_kwargs': {
        'username': os.getenv('PROXY_USERNAME'),
        'password': os.getenv('PROXY_PASSWORD')
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def get_constellation_name(update, context):
    user_text = update.message.text
    user_text = user_text.split()[-1]
    if user_text.lower() == 'mercury':
        planet = ephem.Mercury()
    if user_text.lower() == 'venus':
        planet = ephem.Venus()
    if user_text.lower() == 'mars':
        planet = ephem.Mars()
    if user_text.lower() == 'jupiter':
        planet = ephem.Jupiter()
    if user_text.lower() == 'saturn':
        planet = ephem.Saturn()
    if user_text.lower() == 'uranus':
        planet = ephem.Uranus()
    if user_text.lower() == 'neptune':
        planet = ephem.Neptune()

    planet.compute()
    constellation = ephem.constellation(planet)[1]
    update.message.reply_text(f'{planet.name} находится в созвездии {constellation}')


def main():
    mybot = Updater(os.getenv('TG_TOKEN'), request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', get_constellation_name))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()
    get_constellation_name()


if __name__ == '__main__':
    main()
