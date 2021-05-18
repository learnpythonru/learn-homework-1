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
from datetime import date
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

def planet(update, context):
    user_text = update.message.text   
    
    if user_text.lower() == '/planet марс' or user_text.lower() == '/planet mars':
      mars = ephem.Mars(date.today())
      constellation = ephem.constellation(mars)
      update.message.reply_text(constellation)

    if user_text.lower() == '/planet венера' or user_text.lower() == '/planet venus':
      venus = ephem.Venus(date.today())
      constellation = ephem.constellation(venus)
      update.message.reply_text(constellation) 

    if user_text.lower() == '/planet меркурий' or user_text.lower() == '/planet mercury':
      mercury = ephem.Mercury(date.today())
      constellation = ephem.constellation(mercury)
      update.message.reply_text(constellation)

    if user_text.lower() == '/planet юпитер' or user_text.lower() == '/planet jupiter':
      jupiter = ephem.Jupiter(date.today())
      constellation = ephem.constellation(jupiter)
      update.message.reply_text(constellation)

    if user_text.lower() == '/planet сатурн' or user_text.lower() == '/planet saturn':
      saturn = ephem.Saturn(date.today())
      constellation = ephem.constellation(saturn)
      update.message.reply_text(constellation)
     
    if user_text.lower() == '/planet уран' or user_text.lower() == '/planet uranus':
      uranus = ephem.Uranus(date.today())
      constellation = ephem.constellation(uranus)
      update.message.reply_text(constellation)

    if user_text.lower() == '/planet нептун' or user_text.lower() == '/planet neptune':
      neptune = ephem.Neptune(date.today())
      constellation = ephem.constellation(neptune)
      update.message.reply_text(constellation)
   


def main():
    mybot = Updater("1821940905:AAFnxRktxDNd3hMSmGnN-M2BmQrhymnfdME", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
