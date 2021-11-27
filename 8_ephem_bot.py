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
import datetime
import logging

import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from mybot import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
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


def planet_info(update, context):

    received_text = update.message.text.split()
    having_planets = ephem._libastro.builtin_planets()
    ephem_planets = [name for _0, _1, name in having_planets]

    for planet in received_text:
        planet_name = planet.lower().capitalize()

        if planet_name in ephem_planets:
            if planet_name == 'Mars':
                planet=ephem.Mars()
            elif planet_name == 'Mercury':
                planet = ephem.Mercury()
            elif planet_name == 'Venus':
                planet = ephem.Venus()
            elif planet_name == 'Jupiter':
                planet = ephem.Jupiter()
            elif planet_name == 'Saturn':
                planet = ephem.Saturn()
            elif planet_name == 'Uranus':
                planet = ephem.Uranus()
            elif planet_name == 'Neptune':
                planet = ephem.Neptune()
            elif planet_name == 'Pluto':
                planet = ephem.Pluto()
            elif planet_name == 'Sun':
                planet = ephem.Sun()
            elif planet_name == 'Moon':
                planet = ephem.Moon()
            else:
                print(f'Данные по планете {planet} потерялись)')

            today = datetime.datetime.now()
            now = today.strftime("%Y/%m/%d")
            planet.compute(now)
            answer = ephem.constellation(planet)
            update.message.reply_text(f"Сегодня {now} планета {planet_name} находится в созвездии {answer}")

        elif planet_name == '/planet':
            pass

        else:
            update.message.reply_text(f"Нет такой планеты '{planet_name}'")



def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", planet_info))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
