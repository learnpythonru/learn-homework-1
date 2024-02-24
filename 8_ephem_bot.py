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
from datetime import date

import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

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
    update.message.reply_text(user_text)


def get_planet_constellation(update, context):
    user_text = update.message.text.split()[1]
    print(user_text)
    if user_text == 'Mercury':
        constellation = ephem.constellation(ephem.Mercury(date.today()))
    elif user_text == "Venus":
        constellation = ephem.constellation(ephem.Venus(date.today()))
    elif user_text == 'Mars':
        constellation = ephem.constellation(ephem.Mars(date.today()))
    elif user_text == "Jupiter":
        constellation = ephem.constellation(ephem.Jupiter(date.today()))
    elif user_text == "Saturn":
        constellation = ephem.constellation(ephem.Jupiter(date.today()))
    elif user_text == "Uranus":
        constellation = ephem.constellation(ephem.Uranus(date.today()))
    elif user_text == "Neptune":
        constellation = ephem.constellation(ephem.Neptune(date.today()))
    update.message.reply_text(f"Сегодня {user_text} в созвездии {constellation[1]}")


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
