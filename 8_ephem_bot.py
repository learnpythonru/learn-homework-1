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
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print('Вызван /start')
    print(update)
    update.message.reply_text('Здравствую, пользователь!')

def tolk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def get_planet(update, context):
    print('Вызванна команда /planet')
    print(update)
    text = update.message.text.split()
    planet = text[1]
    date = datetime.datetime.now()
    if planet.lower() == 'mars':
        m = ephem.Mars(date)
        update.message.reply_text(ephem.constellation(m))


def main():
    mybot = Updater(settings.API_KEY, use_context=True) #request_kwargs=PROXY

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', get_planet))
    dp.add_handler(MessageHandler(Filters.text, tolk_to_me))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if  __name__ == '__main__':
    main()


if __name__ == "__main__":
    main()
