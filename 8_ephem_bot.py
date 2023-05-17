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
import time
from datetime import date
import settings
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.Formatter.converter = time.gmtime
logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    datefmt='%d.%m.%Y %H:%M:%S',
    format='%(asctime)s (GMT+0) %(message)s',
    encoding='utf-8'
)


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Здравствуй, пользователь!')


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def check_current_planet_constellation(update, context):
    current_date = date.today()
    ephem_planets = {
        'mars': ephem.Mars,
        'mercury': ephem.Mercury,
        'venus': ephem.Venus,
        'jupiter': ephem.Jupiter,
        'saturn': ephem.Saturn,
        'uranus': ephem.Uranus,
        'neptune': ephem.Neptune
    }
    planet = update.message.text.split()[1].lower()

    if planet in ephem_planets:
        update.message.reply_text(
            f'Today {planet.capitalize()} is in {ephem.constellation(ephem_planets[planet](current_date))}'
        )


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', check_current_planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
