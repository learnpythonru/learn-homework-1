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
from datetime import datetime, date
import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


# PROXY = {
#   'proxy_url': 'socks5://t1.learn.python.ru:1080',
#  'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def planet_finding(update, context):
    text = 'Вызван /planet'
    print(text)
    update.message.reply_text("Про какую плаету ты хочешь узнать?")


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    today = datetime.date(datetime.now())
    mars = ephem.Mars(today)
    const_mars = ephem.constellation(mars)
    venus = ephem.Venus(today)
    const_venus = ephem.constellation(venus)
    jupiter = ephem.Jupiter(today)
    const_jupiter = ephem.constellation(jupiter)
    saturn = ephem.Saturn(today)
    const_saturn = ephem.constellation(saturn)
    planet_list = {'Venus': const_venus, 'Mars': const_mars,
                   'Jupiter': const_jupiter, 'Saturn': const_saturn}
    ask_user = str(user_text).lower().capitalize()
    ask_user_1 = ask_user.split(' ')
    if planet_list.get(str(ask_user_1[0])) == None:
        ask_user_1
    else:
        try:
            update.message.reply_text(
                f'Планта сейчас находится в созвездии: {planet_list.get(str(ask_user_1[0]))}')
        except:
            if planet_list.get(str(ask_user_1[1])) == None:
                ask_user_1
            else:
                update.message.reply_text(
                    f'Планта сейчас находится в созвездии: {planet_list.get(str(ask_user_1[1]))}')


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("planet", planet_finding))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
