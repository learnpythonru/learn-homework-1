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
import json
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
)


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    update.message.reply_text(user_text)


def planet_command(bot, update):
    planet_name = update.message.text.split()[1]
    logging.info("Planet command used, the planet is %s.", planet_name)
    planet_catalog = {
        "Moon": ephem.Moon,
        "Mercury": ephem.Mercury,
        "Venus": ephem.Venus,
        "Mars": ephem.Mars,
        "Jupiter": ephem.Jupiter,
        "Saturn": ephem.Saturn,
        "Uranus": ephem.Uranus,
        "Neptune": ephem.Neptune,
        "Pluto": ephem.Neptune
    }
    planet_class = planet_catalog.get(planet_name)
    if planet_class is not None:
        planet = planet_class()
        planet.compute()
        update.message.reply_text(ephem.constellation(planet)[1])
    else:
        update.message.reply_text("Неизвестная планета")


def main():
    with open("settings.json") as settings_file:
        settings = json.load(settings_file)
    key = settings["KEY"]
    proxy_settings = settings["PROXY"]
    mybot = Updater(key, request_kwargs=proxy_settings)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_command))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
