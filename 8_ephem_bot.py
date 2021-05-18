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


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def get_planet_info(update, context):
    text = update.message.text
    planet_name = text.split()[1]
    if planet_name == 'Moon':
      planet = ephem.Moon(datetime.today())

    if planet_name == 'Mars':
      planet = ephem.Mars(datetime.today())

    if planet_name == 'Saturn':
      planet = ephem.Saturn(datetime.today())

    if planet_name == 'Venus':
      planet = ephem.Venus(datetime.today())

    if planet_name == 'Pluto':
      planet = ephem.Pluto(datetime.today())

    if planet_name == 'Jupiter':
      planet = ephem.Jupiter(datetime.today())

    if planet:
      const = ephem.constellation(planet)
      update.message.reply_text(f'Планета {planet_name} находится в созвездии {const}')
    else:
      update.message.reply_text('Повторите запрос')


def main():
    mybot = Updater("КЛЮЧ, КОТОРЫЙ НАМ ВЫДАЛ BotFather", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet_info))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
