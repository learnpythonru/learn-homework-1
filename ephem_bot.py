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
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def echo_planet(bot, update):
    text = 'Вызвана команда /planet'
    user_input = update.message.text.split()[-1]
    if user_input == 'Mars':
        planet = ephem.Mars(datetime.datetime.now().strftime("%d/%m/%Y"))
        const = ephem.constellation(planet)
        if const[1] == 'Aquarius':
            const = 'Марс находится в созвездии стрельцов'
            update.message.reply_text(const)


def main():
    mybot = Updater("964732996:AAFq8h7ibvfHdoTrHf9sZsejh4eDaY3dJW8")

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", echo_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()