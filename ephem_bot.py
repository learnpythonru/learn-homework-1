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
import datetime
import settings
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)

def greet_user(bot, update):
    text = 'Вызван /start'
    update.message.reply_text(text)


def get_planet(bot, update):
    answer = 'Не знаю такую планету'
    today = datetime.datetime.now().strftime('%Y/%d/%m')
    planet = update.message.text.split()
    if len(planet) > 1 and planet[1].lower() == 'mars':
        mars = ephem.Mars(today)
        update.message.reply_text('{} :: {}'.format(today, ephem.constellation(mars)))
    else:
        update.message.reply_text(answer)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 

def main():
    mybot = Updater(settings.BOT_TOKEN, request_kwargs=settings.PROXY)
    
    dp = mybot.dispatcher  
    dp = mybot.dispatcher  
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
