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
import bot_info
import logging, ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def get_planet(update, context):
    # chosen_planet = update.message.text.split()[1]
    date = datetime.now().strftime('%Y/%M/%d')

    try:
        chosen_planet = context.args[0].capitalize()
    except IndexError:
        chosen_planet = ''
    
    if chosen_planet in ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']:
        if chosen_planet == "Mercury":
            planet_constellation = ephem.constellation(ephem.Mercury(date))
        elif chosen_planet == "Venus":
            planet_constellation = ephem.constellation(ephem.Venus(date))
        elif chosen_planet == "Mars":
            planet_constellation = ephem.constellation(ephem.Mars(date))
        elif chosen_planet == "Jupiter":
            planet_constellation = ephem.constellation(ephem.Jupiter(date))
        elif chosen_planet == "Saturn":
            planet_constellation = ephem.constellation(ephem.Saturn(date))
        elif chosen_planet == "Uranus":
            planet_constellation = ephem.constellation(ephem.Uranus(date))
        elif chosen_planet == "Neptune":
            planet_constellation = ephem.constellation(ephem.Neptune(date))
        elif chosen_planet == "Pluto":
            planet_constellation = f'Плутон больше не планета, но он находится в созвездии {ephem.constellation(ephem.Pluto(date))}'
    else:
        planet_constellation = "Введите название планеты на английском"

    update.message.reply_text(planet_constellation)
    

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(bot_info.token, request_kwargs=bot_info.PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
