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
from datetime import datetime
from typing import Type
import Setting
import logging
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')



def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)

def planet_mars(update, context):
    planet = update.message.text.split()
    try:
      planet_ephem = getattr(ephem,planet[1].lower().capitalize())(datetime.now())
    
      constellation = ephem.constellation(planet_ephem)
      
      text = f"Планета {planet[1].lower().capitalize()} находится в {constellation}"
    except AttributeError:
      text = f"Планета {planet[1].lower().capitalize()} не найдена."
    update.message.reply_text(text)

def main():
    mybot = Updater(Setting.API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_mars))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
