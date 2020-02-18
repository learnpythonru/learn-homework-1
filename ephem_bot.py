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
import logging, ephem
from my_data import API_KEY, PROXY
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


PLANETS_MAP = {
    'mars': ephem.Mars(),
    'venus': ephem.Venus(),
    'mercury': ephem.Mercury(),
    'jupiter': ephem.Jupiter(),
    'saturn': ephem.Saturn(),
    'uranus': ephem.Uranus(),
    'neptune': ephem.Neptune(),
}


def find_cons(bot, update):
    if len(update.message.text.split()) == 2:
        name_planet = update.message.text.split()[1]
        planet = name_planet.lower()
        if planet in PLANETS_MAP:
            temp = PLANETS_MAP[planet]
            temp.compute()
            constellation = ephem.constellation(temp)
            update.message.reply_text(constellation[1])
        else:
            update.message.reply_text('Этой планеты нет в Солнечной системе :)')


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", find_cons))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
