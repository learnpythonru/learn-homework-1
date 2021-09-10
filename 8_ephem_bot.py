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
    text = '''Это астрономический бот! Введите /planet <planet> и узнаете в каком созвездии расположена планета сегодня! Например /planet mars'''
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def get_constellation(update, context):
    planets = {
        "mercury":ephem.Mercury,
        "venus":ephem.Venus,
        "mars":ephem.Mars,
        "jupiter":ephem.Jupiter,
        "saturn":ephem.Saturn,
        "uranus":ephem.Uranus,
        "neptune":ephem.Neptune
    }
    try:
        planet = update.message.text.split()[1].lower()
    except IndexError:
        update.message.reply_text("введите планету в формате /planet <planet>")
    
    if planet not in planets:
        update.message.reply_text("неизвестная планета")
    
    today_planet = planets[planet](datetime.today().strftime("%Y/%m/%d"))
    constellation = ephem.constellation(today_planet)
    update.message.reply_text(constellation)


def main():
    mybot = Updater(os.getenv('KEY'),
                    request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
