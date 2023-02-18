import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings
import ephem


logging.basicConfig(filename="bot.log", level = logging.INFO)

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет пользователь')

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)

    p = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if user_text in p: 
        update.message.reply_text("Введите дату")
        b = update.message.text 
        print(b)
        if user_text == "Mercury":
            f = ephem.Mercury(b)
        elif user_text == "Venus":
            f = ephem.Venus(b)
        elif user_text == "Mars":
            f = ephem.Mars(b)
        elif user_text == "Jupiter":
            f = ephem.Jupiter(b)
        elif user_text == "Saturn":
            f = ephem.Saturn(b)
        elif user_text == "Uranus":
            f = ephem.Uranus(b)
        elif user_text == "Neptune":
            f = ephem.Neptune(b)
        constellation = ephem.constellation(f)
        update.message.reply_text(constellation)
    else:
        update.message.reply_text(user_text)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
