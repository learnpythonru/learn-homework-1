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
import os
import re

import ephem
from datetime import datetime
from dotenv import load_dotenv

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

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
    text = '''Это астрономический бот! Введите /planet <planet> и узнаете\
    в каком созвездии расположена планета сегодня! Например /planet mars\
    Так же можно узнать про следующую полную фазу луны формате /next_full_moon гггг-мм-дд'''
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def get_constellation(update, context):
    raw_planet = None
    try:
        raw_planet = update.message.text.split()[-1].strip().capitalize()
    except IndexError:
        update.message.reply_text("введите планету в формате /planet <planet>")

    planet = getattr(ephem, raw_planet, None)
    if not planet:
        update.message.reply_text("неизвестная планета")
    else:
        today_planet = planet(datetime.today().strftime("%Y/%m/%d"))
        constellation = ephem.constellation(today_planet)
        update.message.reply_text(constellation)


def get_fool_moon(update, context):
    raw_date = update.message.text.split()[-1]
    if not re.fullmatch(r'\d\d\d\d-\d\d-\d\d', raw_date):
        update.message.reply_text("введите дату в формате /next_full_moon гггг-мм-дд")
    else:
        full_moon_date = ephem.next_full_moon(raw_date)
        try:
            update.message.reply_text(str(full_moon_date.datetime()))
        except ValueError:
            update.message.reply_text("введите корректную дату в формате /next_full_moon гггг-мм-дд")


def main():
    ephem_bot = Updater(os.getenv('KEY'),
                        request_kwargs=PROXY, use_context=True)

    dp = ephem_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation))
    dp.add_handler(CommandHandler("next_full_moon", get_fool_moon))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    ephem_bot.start_polling()
    ephem_bot.idle()


if __name__ == "__main__":
    main()
