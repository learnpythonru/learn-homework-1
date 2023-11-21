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
import datetime
import logging

import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


# PROXY = {
#     'proxy_url': 'socks5://t1.learn.python.ru:1080',
#     'urllib3_proxy_kwargs': {
#         'username': 'learn',
#         'password': 'python'
#     }
# }


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Hello')

def planet(update, context):
    text = '/planet'
    print(text)
    update.message.reply_text('Enter planet in English')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def get_planet(update, context):
    date_now = datetime.date.today()
    lst_planet = {'Mercury': ephem.Mercury, 'Venus': ephem.Venus, 'Mars': ephem.Mars,
                  'Jupiter': ephem.Jupiter, 'Saturn': ephem.Saturn, 'Uranus': ephem.Uranus,
                  'Neptune': ephem.Neptune, 'Pluto': ephem.Pluto}
    user_text = update.message.text
    if user_text in lst_planet:
        m = lst_planet[user_text]
        print(user_text)
        update.message.reply_text(ephem.constellation(m(date_now)))
    else:
        print(user_text)
        update.message.reply_text('Nope, try again')


def main():
    mybot = Updater(settings.API_KEY,  use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, get_planet))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
