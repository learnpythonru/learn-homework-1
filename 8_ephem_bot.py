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
import datetime
import logging
import sys

import ephem
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from secret import TOKEN

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    level=logging.INFO,
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)


def greet_user(update, context):
    logger.info("Вызван /start")
    update.message.reply_text(f"Привет, {update.message.from_user.first_name}")


def talk_to_me(update, context):
    update.message.reply_text(update.message.text)


def where_is_planet(update, context):
    planet_names = [
        p[2]
        for p in ephem._libastro.builtin_planets()
        if p[1] == "Planet" and p[2] not in ("Sun", "Moon")
    ]
    planet_name = update.message.text.split()[1].title()
    if planet_name not in planet_names:
        update.message.reply_text(
            f"Not find planet {planet_name}. "
            f'Select one from the options {", ".join(planet_names)}'
        )
    planet = ephem.__dict__[planet_name](datetime.date.today())
    update.message.reply_text(", ".join(ephem.constellation(planet)))


def main():
    logger.info("The bot has started")
    my_bot = Updater(TOKEN)

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", where_is_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    my_bot.start_polling()
    my_bot.idle()  # зацикливает бота


if __name__ == "__main__":
    main()
