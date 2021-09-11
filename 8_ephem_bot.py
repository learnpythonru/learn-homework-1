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
import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def planet (update,context):
    current_date = datetime.now().date().strftime('%d/%m/%Y')   #дата
    
    text = 'Вызван /planet'
    print(text)

    planeta = update.message.text
    planet_needed = planeta.split()[1]

    if planet_needed == 'Mercury':
        mercury = ephem.Mercury(current_date)
        result_final = ephem.constellation(mercury)
        update.message.reply_text(result_final)

    elif planet_needed == 'Venus':
        venus = ephem.Venus(current_date)
        result_final = ephem.constellation(venus)
        update.message.reply_text(result_final)
    
    elif planet_needed == 'Mars':
        mars = ephem.Mars(current_date)
        result_final = ephem.constellation(mars)
        update.message.reply_text(result_final)
    
    elif planet_needed == 'Jupiter':
        jupiter = ephem.Jupiter(current_date)
        result_final = ephem.constellation(jupiter)
        update.message.reply_text(result_final)

    elif planet_needed == 'Saturn':
        saturn = ephem.Saturn(current_date)
        result_final = ephem.constellation(saturn)
        update.message.reply_text(result_final)
    
    elif planet_needed == 'Uranus':
        uranus = ephem.Uranus(current_date)
        result_final = ephem.constellation(uranus)
        update.message.reply_text(result_final)
    
    elif planet_needed == 'Neptune':
        neptune = ephem.Neptune(current_date)
        result_final = ephem.constellation(neptune)
        update.message.reply_text(result_final)
    
    else:
        update.message.reply_text('Введите планету правильно (с большой буквы и на английском')

    


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('planet', planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
