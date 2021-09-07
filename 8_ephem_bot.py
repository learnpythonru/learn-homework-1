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
import warnings
import settings

from datetime import datetime



from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

warnings.filterwarnings("ignore", category=DeprecationWarning) 
dt_now = datetime.now()

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

mercury = ephem.Mercury(dt_now)
venus = ephem.Venus(dt_now)
mars = ephem.Mars(dt_now)
jupiter = ephem.Jupiter(dt_now)
saturn = ephem.Saturn(dt_now)
uranus = ephem.Uranus(dt_now)
neptune = ephem.Neptune(dt_now)

planets = {
  'Mercury': mercury,
  'Venus': venus,
  'Mars': mars,
  'Jupiter': jupiter,
  'Saturn': saturn,
  'Uranus': uranus,
  'Neptune': neptune,
  }

def planet_search(update, context):
    text = 'Вызван /planet'
    update.message.reply_text(text)
    user_text = update.message.text.split()[1]
    if user_text in planets.keys():
      pl = planets[user_text]
      const = ephem.constellation(pl)
      update.message.reply_text(const)

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_search))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
