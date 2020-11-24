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
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.callbackqueryhandler import CallbackQueryHandler
from telegram.callbackquery import CallbackQuery
import bot_settings
import sys

if not sys.warnoptions:
    import warnings

    warnings.simplefilter("ignore")

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

PROXY = {
    'proxy_url': bot_settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': bot_settings.PROXY_USERNAME,
        'password': bot_settings.PROXY_PASSWORD
    }
}


def planet(update, context):
    user_text = update.message.text
    print(type(user_text))
    print(type(user_text.split('')))

    planets = {
        'mercury': ephem.Mercury('2020'),
        'venus': ephem.Venus('2020'),
        'mars': ephem.Mars('2020'),
        'jupiter': ephem.Jupiter('2020'),
        'saturn': ephem.Saturn('2020'),
        'uranus': ephem.Uranus('2020'),
        'neptune': ephem.Neptune('2020')
    }

    def ask_user(answers_dict, text):
        user_text = text
        for que, ans in answers_dict.items():
            if que == user_text:
                return ans

    const = ephem.constellation(ask_user(planets, user_text))
    update.message.reply_text(const)


def greet_user(update, context):
    text = 'Привет, я твой ботец!'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(bot_settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Ботушка стартонул!")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
