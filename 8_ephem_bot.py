import logging
import ephem
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    update.message.reply_text('Здравствуй пользователь!')

def talk_to_me(update, context):
    text = update.message.text
    update.message.reply_text(text)

def planetary_constellation(update, context):
    current_date = date.today()
    planet_name = update.message.text.split()[-1].capitalize()
    planet = getattr(ephem, planet_name)(current_date)
    constellation = ephem.constellation(planet)
    update.message.reply_text(f'Планета {planet_name} находиться в созвездии: {constellation[-1]}')

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planetary_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('bot started')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()