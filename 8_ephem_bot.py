import logging
import string
import ephem
import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


# PROXY = {
#     'proxy_url': settings.PROXY_URL',
#     'urllib3_proxy_kwargs': {
#     'username': settings.PROXY_USERNAME,
#     'password': settings.PROXY_PASSWORD
#     }
# }


def greet_user(update, context):
    update.message.reply_text('Вызван /start')


def talk_to_me(update, context):
    update.message.reply_text(update.message.text)


def constel(update, context):

    planet_key: str = update.message.text.lower().split()[-1]

    planets: dict = {
            'mercury': ephem.Mercury,
            'venus': ephem.Venus,
            'moon': ephem.Moon,
            'sun': ephem.Sun,
            'mars': ephem.Mars,
            'jupiter': ephem.Jupiter,
            'saturn': ephem.Saturn,
            'uranus': ephem.Uranus,
            'neptune': ephem.Neptune,
            'pluto': ephem.Pluto,
            'меркурий': ephem.Mercury,
            'венера': ephem.Venus,
            'луна': ephem.Moon,
            'солнце': ephem.Sun,
            'марс': ephem.Mars,
            'юпитер': ephem.Jupiter,
            'сатурн': ephem.Saturn,
            'уран': ephem.Uranus,
            'нептун': ephem.Neptune,
            'плутон': ephem.Pluto,
        }

    position = planets[planet_key](datetime.today().strftime('%Y/%m/%d'))
    const = ephem.constellation(position)[1]
    update.message.reply_text(f'{planet_key.title()} is in {const} today.')


def word_counter(update, context):

    res: str = ''

    for i in update.message.text:
        if i in string.punctuation:
            res += ' '
        else:
            res += i

    message_length: int = len(res.split()) - 1

    if message_length < 1:
        update.message.reply_text("Недостаточно слов для подсчета, введите текст: ")
    else:
        if message_length in range(11, 21) or str(message_length)[-1] in '056789':
            update.message.reply_text(f"{message_length} слов")
        elif str(message_length)[-1] == '1':
            update.message.reply_text(f"{message_length} слово")
        else:
            update.message.reply_text(f"{message_length} слова")


def main():
    mybot = Updater(
        settings.API_KEY,
        # request_kwargs=PROXY,
        use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", constel))
    dp.add_handler(CommandHandler("wordcount", word_counter))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот запущен')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    print('Бот запущен!')
    main()
