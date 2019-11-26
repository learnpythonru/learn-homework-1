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
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
import time



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def search_planet(bot, update):
   
    planet = update.message.text.split()[-1]
    now_date = time.strftime('%Y/%m/%d')
    print(planet, now_date)
    if planet == 'Mercury':
        ep_planet = ephem.Mercury(now_date)
    elif planet == 'Venus':
        ep_planet = ephem.Venus(now_date)
    elif planet == 'Mars':
        ep_planet = ephem.Mars(now_date)
    elif planet == 'Jupiter':
        ep_planet = ephem.Jupiter(now_date)
    elif planet == 'Saturn':
        ep_planet = ephem.Saturn(now_date)
    elif planet == 'Uranus':
        ep_planet = ephem.Uranus(now_date)
    elif planet == 'Neptune':
        ep_planet = ephem.Neptune(now_date)
    else:
        print('Ввод неверный')
    const = ephem.constellation(ep_planet)
    print(const)
    user_text_const = f'Планета {planet} сегодня находится в созвездии {const}'
    print(user_text_const)
    update.message.reply_text(user_text_const)


def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat id %s, Message: %s", update.message.chat.username,
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    
    logging.info('Бот запускается')
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('planet', search_planet))
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
   

    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
