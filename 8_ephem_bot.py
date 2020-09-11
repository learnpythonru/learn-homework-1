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
                    filename='bot.log'
)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def planet(bot, update):
    dict_planets = {'Mercury' : ephem.Mercury, 
                    'Venus'   : ephem.Venus, 
                    'Mars'    : ephem.Mars, 
                    'Jupiter' : ephem.Jupiter, 
                    'Saturn'  : ephem.Saturn, 
                    'Uranus'  : ephem.Uranus, 
                    'Neptune' : ephem.Neptune,
                    'Pluto'   : ephem.Pluto}
    user_planet = update.message.text.split()[1].lower().capitalize()
    if user_planet in dict_planets:
      constellation = ephem.constellation(dict_planets[user_planet](date.today()))
      reply_text = f'{user_planet} is currently in the constellation of {constellation[1]}'
    else:
      reply_text = 'Unknown planet...'
    update.message.reply_text(reply_text)

if __name__ == "__main__":
    main()
