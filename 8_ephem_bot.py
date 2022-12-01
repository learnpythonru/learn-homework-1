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
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv("API_KEY_PLANET_BOT")

from datetime import datetime

planet_aliases = {
    "Марс": "Mars",
    "Уран": "Uranus",
    "Юпитер": "Jupiter",
    "Меркурий": "Mercury",
    "Сатурн": "Saturn",
    "Нептун": "Neptune"
}


def get_planet_constellation(planet_alias):
    today = datetime.today().strftime('%Y/%m/%d')

    planet_name = planet_aliases.get(planet_alias, planet_alias)
    print(planet_name)

    #planets
    planet_attr = getattr(ephem, planet_name, None)
    if not planet_attr:
        return None

    planet = planet_attr(today)
    constellation = ephem.constellation(planet)
    return constellation


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def greet_user(update, context):
    text = "Привет,  напиши название планеты в формате 'Марс'"
    update.message.reply_text(text)

def talk_to_me(update, context):
    constellation = get_planet_constellation(update.message.text)
    if not constellation:
        update.message.reply_text("Я тебя не понимаю. Напиши /start.")
        return
    update.message.reply_text(constellation[1] )


def main():
    mybot = Updater(API_KEY
, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()



if __name__ == "__main__":
    main()
