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
import setting

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')




def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def galaxy(update, context):
    planet_list = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    mistake = 'Введите название планеты'
    planet = (update.message.text).split()
    if len(planet) == 2:
        your_planet = planet[1]
        if your_planet in planet_list:
            date = datetime.now()
            planet_func=getattr(ephem, your_planet)(date)
            your_galaxy = ephem.constellation(planet_func)
            print(your_galaxy)
            update.message.reply_text(your_galaxy[1])
        else:
            print(mistake)
            update.message.reply_text(mistake)
    else:
        print(mistake)
        update.message.reply_text(mistake)

        
    print(planet)
    


def main():
    mybot = Updater(setting.API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", galaxy))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
