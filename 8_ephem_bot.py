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
import ephem
from ephem import *
from datetime import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from decouple import config

TOKEN = config('TOKEN')

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


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def planet_user(update, context):
    text = 'Вызван /planet'
    user_text = update.message.text
    planet_user = user_text.split(sep=" ")
    all_planets = [name for _0, _1, name in ephem._libastro.builtin_planets()]
    if planet_user[1] in all_planets :
        planet = getattr(ephem, planet_user[1])() 
        planet.compute(datetime.now())
        res = ephem.constellation(planet)
        update.message.reply_text(res)
    else:
        update.message.reply_text("Please enter correct planet or star")


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(TOKEN, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("planet", planet_user))
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
