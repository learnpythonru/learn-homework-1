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
import config
import ephem
import datetime

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


def info_planet(update, context):
    planet = 1
    text = (update.message.text).split()[planet]
    print(f"Call /planet {text}")

    planet_list = [name for _, _, name in ephem._libastro.builtin_planets()]

    if text in planet_list:
        planet_object = getattr(ephem, text)()

        now_date = datetime.datetime.now().strftime('%Y/%m/%d')
        planet_object.compute(now_date)

        _, constellation = ephem.constellation(planet_object)

        update.message.reply_text(f"Planet {text} is in the constellation {constellation}")

    else:
        update.message.reply_text(f"'{text}' is not a planet. Request format: Mars, Saturn, etc")



def main():
    mybot = Updater(config.TELEGRAM_API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", info_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
