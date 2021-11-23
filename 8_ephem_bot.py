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

from datetime import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import ephem

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


def planet_constellation(update, context): 
    try:
        command, planet = update.message.text.split()
        planet_info = getattr(ephem, planet.title())(datetime.now().date())
        cons, constellation = ephem.constellation(planet_info)
        update.message.reply_text(constellation)
    except AttributeError:
        update.message.reply_text("Такой планеты нет")
    except IndexError:
        update.message.reply_text("Вы не ввели название планеты")


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater("КЛЮЧ, КОТОРЫЙ НАМ ВЫДАЛ BotFather",
                    request_kwargs=PROXY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
