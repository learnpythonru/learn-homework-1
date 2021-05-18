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


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def in_which_constellation(update, context):
    user_text = update.message.text
    planet = user_text.split()[1]
    print(f'Запрошено: {planet}')
    date_now = date.today()
    if planet == 'Jupiter':
        update.message.reply_text(f'В созвездии {ephem.constellation(ephem.Jupiter(date_now))[1]}')
    elif planet == 'Mars':
        update.message.reply_text(f'В созвездии {ephem.constellation(ephem.Mars(date_now))[1]}')
    elif planet == 'Mercury':
        update.message.reply_text(f'В созвездии {ephem.constellation(ephem.Mercury(date_now))[1]}')
    elif planet == 'Moon':
        update.message.reply_text(f'В созвездии {ephem.constellation(ephem.Moon(date_now))[1]}')
    elif planet == 'Neptune':
        update.message.reply_text(f'В созвездии {ephem.constellation(ephem.Neptune(date_now))[1]}')
    elif planet == 'Pluto':
        update.message.reply_text(f'В созвездии {ephem.constellation(ephem.Pluto(date_now))[1]}')
    elif planet == 'Uranus':
        update.message.reply_text(f'В созвездии {ephem.constellation(ephem.Uranus(date_now))[1]}')
    elif planet == 'Saturn':
        update.message.reply_text(f'В созвездии {ephem.constellation(ephem.Saturn(date_now))[1]}')
    elif planet == 'Venus':
        update.message.reply_text(f'В созвездии {ephem.constellation(ephem.Venus(date_now))[1]}')
    elif planet == 'help':
        update.message.reply_text('Команда /planet работает следующим образом\n'
                                  'Например: /planet Jupiter\n'
                                  'Перечень доступных планет: \nMars,\nMercury,\n'
                                  'Moon,\nNeptune, Pluto,'
                                  '\nSaturn, Uranus, Venus, Jupiter')


def main():
    mybot = Updater(TOKEN, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", in_which_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
