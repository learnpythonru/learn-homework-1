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
from datetime import date

import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

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


def get_planet_constellation(update, context):
    planet_list = [
        'Mercury',
        'Venus',
        'Mars',
        'Jupiter',
        'Saturn',
        'Uranus',
        'Neptune',
    ]

    splited_text = update.message.text.split()
    if len(splited_text) < 2:
        update.message.reply_text("Вы не ввели название планеты")
    elif len(splited_text) > 2:
        update.message.reply_text("Введите название одной планеты")
    else:
        edited_text = splited_text[1].lower()
        print(edited_text)
        if edited_text == 'mercury':
            planet = ephem.Mercury(date.today())
        elif edited_text == 'venus':
            planet = ephem.Venus(date.today())
        elif edited_text == 'mars':
            planet = ephem.Mars(date.today())
        elif edited_text == 'jupiter':
            planet = ephem.Jupiter(date.today())
        elif edited_text == 'saturn':
            planet = ephem.Jupiter(date.today())
        elif edited_text == 'uranus':
            planet = ephem.Uranus(date.today())
        elif edited_text == 'neptune':
            planet = ephem.Neptune(date.today())
        else:
            update.message.reply_text(f"{edited_text} не является планетой. Введите планету из списка {planet_list}")

        update.message.reply_text(f"Сегодня {edited_text.capitalize()} в созвездии {ephem.constellation(planet)[1]}")


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
