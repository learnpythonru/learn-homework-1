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
import ephem
import logging
from settings import API_KEY
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(f'Привет {update["message"]["chat"]["first_name"]}. {text}')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def constellation_planet(update, context):
    planets_name = {
        'mars': ephem.Mars,
        'mercury': ephem.Mercury,
        'venus': ephem.Venus,
        'jupiter': ephem.Jupiter,
        'saturn': ephem.Saturn,
        'uranus': ephem.Uranus,
        'neptune': ephem.Neptune
    }
    planet = update.message.text.split()[1].lower()

    if planet in planets_name:
        update.message.reply_text(
            f'Планета {planet.capitalize()} находится в созведии {ephem.constellation(planets_name[planet](date.today()))}'
        )


def main():
    mybot = Updater(API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", constellation_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
