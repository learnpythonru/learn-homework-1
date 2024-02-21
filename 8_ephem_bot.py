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
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime
from settings import token


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

    
def name_planet(update, **kwargs):
    text_from_user = update.message.text
    logging.info(text_from_user)
    planet = str(text_from_user)
    result=''
    date=datetime.datetime.now()
    if planet == '/planet Earth':
        result = 'Я не знаю, загугли'
    elif planet == '/planet Mercury':
        result = ephem.constellation(ephem.Mercury(date))
    elif planet == '/planet Venus':
        result = ephem.constellation(ephem.Venus(date))
    elif planet == '/planet Mars':
        result = ephem.constellation(ephem.Mars(date))
    elif planet == '/planet Jupiter':
        result = ephem.constellation(ephem.Jupiter(date))
    elif planet == '/planet Saturn':
        result = ephem.constellation(ephem.Saturn(date))
    elif planet == '/planet Uranus':
        result = ephem.constellation(ephem.Uranus(date))
    elif planet == '/planet Neptune':
        result = ephem.constellation(ephem.Neptune(date))
    update.message.reply_text(result)

def main():
    updater=Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("planet", name_planet))
    updater.start_polling()
    updater.idle()
main()
