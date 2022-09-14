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
from time import time
from datetime import datetime
from Setting import APIKEY
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem

logging.basicConfig(
    format="%(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filename="bot.log",
)


def get_planet(planet):
    time_now = datetime.now()
    planet_dict = {
        "Mars": ephem.Mars(time_now),
        "Venus": ephem.Venus(time_now),
        "Saturn": ephem.Saturn(time_now),
        "Jupiter": ephem.Jupiter(time_now),
        "Neptune": ephem.Neptune(time_now),
        "Uranus": ephem.Uranus(time_now),
        "Mercury": ephem.Mercury(time_now),
    }
    return planet_dict.get(planet, None)


def greet_user(update, context):
    text = "Вызван /start"
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planets(update, context):
    text_lst = update.message.text.split()
    if len(text_lst) == 2:
        planetname = update.message.text.split()[1]
        if get_planet(planetname) is not None:
            constellation = ephem.constellation(get_planet(planetname))
            update.message.reply_text(constellation[1])
            update.message.reply_text("Такой планеты нет")
    else:
        update.message.reply_text("Такой команды нет")


def main():
    mybot = Updater(APIKEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planets))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
