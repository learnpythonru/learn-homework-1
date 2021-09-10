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
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config
import time
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

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)

def where_is_planet(update, context):
    today = time.strftime('%Y/%m/%d')
    user_text = update.message.text
    print(user_text)
    planet = (user_text.split()[1])
    update.message.reply_text(user_text.split()[1])
    if planet in ['Mars', 'Jupiter', 'Mercury', 'Pluto']:
        if planet == 'Mars': planet = ephem.Mars(today)
        elif planet == 'Jupiter': planet = ephem.Jupiter(today)
        elif planet == 'Mercury': planet = ephem.Mercury(today)
        elif planet == 'Pluto': planet = ephem.Pluto(today)
        constellation = ephem.constellation(planet)
        print(constellation)
        update.message.reply_text(constellation)

def main():
    mybot = Updater(config.TOKEN, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('planet', where_is_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()