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
import datetime

if not sys.warnoptions:
    import warnings

    warnings.simplefilter("ignore")

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

#Чтобы вывести весь список планет!
#pprint(ephem._libastro.builtin_planets())
#pprint([name for _0, _1, name in ephem._libastro.builtin_planets()])

PROXY = {
    'proxy_url': bot_settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': bot_settings.PROXY_USERNAME,
        'password': bot_settings.PROXY_PASSWORD
    }
}


def planet(update, context):
    user_planet = update.message.text.split()

    try:
        planet = getattr(ephem, user_planet[1])()
        planet.compute(ephem.Date(datetime.date.today()))
        result = ephem.constellation(planet)
        update.message.reply_text(f'Планета {user_planet[1]} в созвездии {result[1]}.')

    except:
        update.message.reply_text(f'Планета {user_planet[1]} не найдена.')


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
