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


def galaxy(planet_user):
    if planet_user.lower() == 'mercury':
        planet = ephem.Mercury(datetime.now())
        constellation = ephem.constellation(planet)
    elif planet_user.lower() == 'venus':
        planet = ephem.Venus(datetime.now())
        constellation = ephem.constellation(planet)
    elif planet_user.lower() == 'earth':
        planet = ephem.Earth(datetime.now())
        constellation = ephem.constellation(planet)
    elif planet_user.lower() == 'mars':
        planet = ephem.Mars(datetime.now())
        constellation = ephem.constellation(planet)
    elif planet_user.lower() == 'jupiter':
        planet = ephem.Jupiter(datetime.now())
        constellation = ephem.constellation(planet)
    elif planet_user.lower() == 'saturn':
        planet = ephem.Saturn(datetime.now())
        constellation = ephem.constellation(planet)
    elif planet_user.lower() == 'uranus':
        planet = ephem.Uranus(datetime.now())
        constellation = ephem.constellation(planet)
    elif planet_user.lower() == 'neptune':
        planet = ephem.Neptune(datetime.now())
        constellation = ephem.constellation(planet)
    else:
        return f'Такой планеты нет в Солнечной системе'

    return f'Сегодня планета находится в созвездии {constellation[1]}'


def talk_to_user(update, context):
    user_call = update.message.text.split()
    if user_call[0] == '/start':
        text = 'Вызван /start'
    elif user_call[0] == '/planet':
        text = galaxy(user_call[1])
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    update.message.reply_text(user_text)


def main():
    mybot = Updater("1994879172:AAFCprXlFGh8Kyr5aECDrEvGHjS6fa4rSuI", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", talk_to_user))
    dp.add_handler(CommandHandler("planet", talk_to_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
