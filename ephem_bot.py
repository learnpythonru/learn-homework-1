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
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 
def constellation_today(bot, update):
    user_text = update.message.text
    text = user_text.split()
    text1 = 'Вызван /planet'
    print(text1)
    update.message.reply_text(text1)
    now = str(date.today())
    now = now.replace('-','/') 
    planet = getattr(ephem, text[1])(now)
    constellation_planet = ephem.constellation(planet)
    update.message.reply_text(constellation_planet)
    
def main():
    mybot = Updater("1017943578:AAFSaBEhIBPLVK-epDLFoWpthzNNdKhkk5k", request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    dp.add_handler(CommandHandler("planet", constellation_today))

    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
