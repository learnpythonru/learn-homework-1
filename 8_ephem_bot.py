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
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date
from settings import TOKEN, PROXY

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


def in_which_constellation(update, context):
    user_text = update.message.text.split()[1].capitalize()
    date_now = date.today()
    planet = getattr(ephem, user_text)
    constellation = ephem.constellation(planet(date_now))[1]
    update.message.reply_text(f'Планета {user_text} в созвездии {constellation}')


def helper(update, context):
    update.message.reply_text('Команда /planet работает следующим образом\nНапример: /planet Jupiter\n'
                              'А так же: \nMars,\nMercury,\nMoon,\nNeptune, Pluto,'
                              '\nSaturn, Uranus, Venus, Jupiter')


def main():
    mybot = Updater(TOKEN, request_kwargs=PROXY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", in_which_constellation))
    dp.add_handler(CommandHandler("help", helper))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
