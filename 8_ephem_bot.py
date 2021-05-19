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
    
    planet_dict = {
      '/planet марс': ephem.Mars(date.today()), '/planet венера': ephem.Venus(date.today()),
      '/planet меркурий': ephem.Mercury(date.today()), '/planet юпитер': ephem.Jupiter(date.today()),
      '/planet сатурн': ephem.Saturn(date.today()), '/planet уран': ephem.Uranus(date.today()),
      '/planet нептун': ephem.Neptune(date.today()) 
     }
    
    if user_text in planet_dict:
      constellation = ephem.constellation(planet_dict[user_text])
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
