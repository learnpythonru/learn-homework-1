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
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
from datetime import date

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


""" PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
} """

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def planet(update, context):
    dt_now = date.today()
    b = update.message.text #(update['message'])['text']
    d = ((b.split())[1]).lower()
    if d == 'mars':
        m = ephem.Mars(dt_now.year)
    elif d == 'mercury':
        m = ephem.Mercury(dt_now.year)
    elif d == 'venus':
        m = ephem.Venus(dt_now.year)
    elif d == 'jupiter':
        m = ephem.Jupiter(dt_now.year)
    elif d == 'saturn':
        m = ephem.Saturn(dt_now.year)
    elif d == 'uranus':
        m = ephem.Uranus(dt_now.year)
    elif d == 'neptune':
        m = ephem.Neptune(dt_now.year)
    elif d == 'pluto':
        m = ephem.Pluto(dt_now.year)
    else:
        update.message.reply_text('Не знаю такую планету')
    update.message.reply_text(ephem.constellation(m))

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
