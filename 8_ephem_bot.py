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

import ephem
import logging

from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

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

planet_dict = {'Mars':ephem.Mars(), 'Uranus':ephem.Uranus(), 'Saturn':ephem.Saturn(), 'Venus':ephem.Venus(),
          'Mercury':ephem.Mercury(), 'Jupiter':ephem.Jupiter(), 'Neptune':ephem.Neptune(), 'Pluto': ephem.Pluto()}

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

"""
def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)
"""

def planet_status(update, context):
      user_text = update.message.text
      planet_giver = user_text.split()[1]
      print(planet_giver)    
      update.message.reply_text('Вы ввели ' + planet_giver)
      if planet_dict.get(planet_giver.capitalize()) != None:
        planet = planet_dict[planet_giver.capitalize()]
        planet.compute(datetime.now())
        print(ephem.constellation(planet))
        update.message.reply_text(ephem.constellation(planet))
      else:
        update.message.reply_text('Такой планеты не существует')     
 



def main():
    mybot = Updater("1962105317:AAGFT9CJFj4B9PF8mKkWilHOg3WQcU9aoQM", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    #dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", planet_status))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
