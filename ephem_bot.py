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

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)

import ephem
import datetime
import settings

def greet_user(bot, update):
    text = '/start command received'
    print(text)
    update.message.reply_text(text)

def find_constellation(bot, update):
    res = update.message.text.split()
    planet = res[1].lower()
    const = 1
    if planet == 'mercury':
        const = ephem.constellation(ephem.Mercury(datetime.datetime.now()))
    elif planet == 'venus':
        const = ephem.constellation(ephem.Venus(datetime.datetime.now()))
    elif planet == 'mars':
        const = ephem.constellation(ephem.Mars(datetime.datetime.now()))
    elif planet == 'jupiter':
        const = ephem.constellation(ephem.Jupiter(datetime.datetime.now()))
    elif planet == 'saturn':
        const = ephem.constellation(ephem.Saturn(datetime.datetime.now()))
    elif planet == 'uranus':
        const = ephem.constellation(ephem.Uranus(datetime.datetime.now()))
    elif planet == 'neptune':
        const = ephem.constellation(ephem.Neptune(datetime.datetime.now()))
    elif planet == 'pluto':
        const = ephem.constellation(ephem.Pluto(datetime.datetime.now()))
    elif planet == 'help':
        const = ('Help', 'Just input a name of the planet after /start\nPlanets available:\n• Mercury\n• Venus\n• Mars\n• Jupiter\n• Satur\n• Uranus\n• Neptune\n• Pluto')
    else:
        const = ('Error', 'No such planet')
    print('user: {}, chat_id: {}, message: {}'.format(update.message.chat.username,
          update.message.chat.id, const[1]))
    update.message.reply_text(const[1])


def talk_to_me(bot, update):
    user_text = update.message.text
    print('user: {}, chat_id: {}, message: {}'.format(update.message.chat.username,
          update.message.chat.id, user_text))
    update.message.reply_text(user_text)
 

def main():
    try:
        mybot = Updater(settings.API_KEY, request_kwargs = settings.PROXY)

        dp = mybot.dispatcher
        dp.add_handler(CommandHandler("start", greet_user))
        dp.add_handler(CommandHandler("planet", find_constellation))
        dp.add_handler(MessageHandler(Filters.text, talk_to_me))
        
        print('Starting the bot')
        mybot.start_polling()
        print('Ready')
        mybot.idle()
    except KeyboardInterrupt:
        print('Goodbye')

if __name__ == "__main__":
    main()
