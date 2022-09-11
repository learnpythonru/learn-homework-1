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

import datetime

import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')



def greet_user(update, context):
    text = 'Вызван /start'
    update.message.reply_text('Здравствуй, пользователь!')


def find_what_constellation_planet(update, context):
    now = datetime.datetime.now()
    planet = update.message.text.split()[-1].capitalize()

    if planet == 'Mercury':
        planet_now = ephem.constellation(ephem.Mercury(now.strftime("%Y-%m-%d")))

    elif planet == 'Venus':
        planet_now = ephem.constellation(ephem.Venus(now.strftime("%Y-%m-%d")))

    elif planet == 'Mars':
        planet_now = ephem.constellation(ephem.Mars(now.strftime("%Y-%m-%d")))

    elif planet == 'Jupiter':
        planet_now = ephem.constellation(ephem.Jupiter(now.strftime("%Y-%m-%d")))

    elif planet == 'Saturn':
        planet_now = ephem.constellation(ephem.Saturn(now.strftime("%Y-%m-%d")))

    elif planet == 'Uranus':
        planet_now = ephem.constellation(ephem.Uranus(now.strftime("%Y-%m-%d")))

    elif planet == 'Neptune':
        planet_now = ephem.constellation(ephem.Neptune(now.strftime("%Y-%m-%d")))

    elif planet == 'Pluto':
        planet_now = ephem.constellation(ephem.Pluto(now.strftime("%Y-%m-%d")))

    elif planet == 'Earth':
        update.message.reply_text(f'Ты и так на {planet}, в небе ее нет.')
        return

    else:
        update.message.reply_text(f'{planet} в солнечной системе нет.')
        return

    update.message.reply_text(f'{planet} сейчас находится в созвездии {planet_now}.')


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", find_what_constellation_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
