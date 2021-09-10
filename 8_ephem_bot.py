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

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime

import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)


def get_planet(update, context): 
    
    user_text = update.message.text
    planet =  user_text.split()[1]
    today = datetime.today() 
    data_day = "{year}/{month}/{day}".format(year = today.year, month = today.month, day = today.day)
    
    dict_of_planets ={
        'Mercury': ephem.Mercury(data_day),
        'Venus': ephem.Venus(data_day),
        'Mars': ephem.Mars(data_day),
        'Jupiter': ephem.Jupiter(data_day),
        'Saturn': ephem.Saturn(data_day),
        'Uranus': ephem.Uranus(data_day),
        'Neptune': ephem.Neptune(data_day),
    }
    
    if planet not in dict_of_planets.keys():
        update.message.reply_text('К сожалению, я не знаю такую планету :(')
    else:
        constellation = ephem.constellation(dict_of_planets[planet])[1]
        update.message.reply_text(f'Сегодня: {data_day}. Планета {planet} в созвездии {constellation}.')


def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Бот стартовал")
    
    
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
