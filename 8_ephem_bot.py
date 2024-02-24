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

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

import ephem
from datetime import date


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log', encoding='utf-8')


PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text("Здравствуй, пользователь!")

def planet_constellation(update, context):
    input_planet = update.message.text.split()[-1].capitalize()

    objects = {'Sun': ephem.Sun,
               'Mercury': ephem.Mercury,
               'Venus': ephem.Venus,
               'Moon': ephem.Moon,
               'Mars': ephem.Mars,
               'Jupiter': ephem.Jupiter,
               'Saturn': ephem.Saturn,
               'Uranus': ephem.Uranus,
               'Neptune': ephem.Neptune,
               'Pluto': ephem.Pluto,
    }
    if input_planet.capitalize() in objects:
        planet = objects[input_planet](date.today().strftime('%Y/%m/%d'))
        const = ephem.constellation(planet)
        update.message.reply_text(f'Сегодня {input_planet} находится в созвездии {const[-1]}.')

    else:
        update.message.reply_text('Такого звездного объекта нет в солнечной системе.')


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
