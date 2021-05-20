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
import settings
import ephem
import datetime

from ephem import *
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}

greetings = """
Hi! This is Ephem bot.
You can specify a planet with
/planet <planet_name>
command and get the constellation where this planet resides now
"""

observer_city = settings.DEFAULT_OBSERVER_CITY


def greet_user(update, context):
    update.message.reply_text(greetings)


def talk_to_me(update, context):
    user_text = update.message.text
    update.message.reply_text('You just said: ' + user_text)


def get_planet(update, context):
    msg = update.message.text.split()
    if len(msg) < 2:
        update.message.reply_text('Missed argument in the /planet command')
    elif len(msg) > 2:
        update.message.reply_text('Too many arguments in the /planet command')
    else:
        cmd, planet = msg
        try:
            update.message.reply_text(planet + ' in ' + get_constellation(planet, observer_city))
        except ValueError as e:
            update.message.reply_text(e.args[0])


def get_constellation(planet, current_city):
    try:
        observer = city(current_city)
    except KeyError:
        raise ValueError('Unknown city specified')
    observer.date = datetime.now()
    try:
        body = getattr(ephem, planet)()
    except AttributeError:
        raise ValueError('Unknown planet name specified')
    try:
        body.compute(observer)
        short_name, full_name = ephem.constellation(body)
    except TypeError:
        raise ValueError('Unknown or small/moon planet name specified')
    return full_name


def main():
    ephem_bot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = ephem_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.log(logging.INFO, "Ephem bot started")

    ephem_bot.start_polling()
    ephem_bot.idle()


if __name__ == "__main__":
    main()
