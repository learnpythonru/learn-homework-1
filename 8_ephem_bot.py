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
import settings

import logging

import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)",
                    level=logging.INFO,
                    filename="bot.log")



def greet_user(update, context):
    text = "Вызван /start"
    print(text)
    update.message.reply_text(text)
    print(update)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


today = "2023/02/18"
def planets(update, context):
    plan_name = update.message.text.split()[1]
    if plan_name == "Mars":
        planet = ephem.Mars(today)
    elif plan_name == "Venus":
        planet = ephem.Venus(today)
    elif plan_name == "Saturn":
        planet = ephem.Saturn(today)
    else:
        update.message.reply_text("Я не знаю такой планеты")
        return
    planet = ephem.constellation(planet)
    logging.info('Вызван /planet')
    update.message.reply_text(planet)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planets))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__": 
    main()
