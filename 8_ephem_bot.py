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

import ephem
import logging
from settings import TOKEN
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

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
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planet(update, context):
    print('Вызван /planet')
    user_text = update.message.text.split()
    # # print(user_text)
    user_planet = user_text[1].capitalize()
    tomorrow = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y/%m/%d')
    if user_planet == 'Mercury':
        constellation = ephem.constellation(ephem.Mercury(tomorrow))
    elif user_planet == 'Venus':
        constellation = ephem.constellation(ephem.Venus(tomorrow))
    elif user_planet == 'Earth':
        constellation = ephem.constellation(ephem.Earth(tomorrow))
    elif user_planet == 'Mars':
        constellation = ephem.constellation(ephem.Mars(tomorrow))
    elif user_planet == 'Jupiter':
        constellation = ephem.constellation(ephem.Jupiter(tomorrow))
    elif user_planet == 'Saturn':
        constellation = ephem.constellation(ephem.Saturn(tomorrow))
    elif user_planet == 'Uranus':
        constellation = ephem.constellation(ephem.Uranus(tomorrow))
    elif user_planet == 'Neptune':
        constellation = ephem.constellation(ephem.Neptune(tomorrow))
    else:
        constellation = f'I dont know planet {user_planet}!'

    update.message.reply_text(constellation)


def main():
    mybot = Updater(TOKEN, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
