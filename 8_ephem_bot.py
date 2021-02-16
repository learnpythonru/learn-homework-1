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
import ephem
import logging
import re
from settings import TOKEN
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


# PROXY = {
#     'proxy_url': 'socks5://t1.learn.python.ru:1080',
#     'urllib3_proxy_kwargs': {
#         'username': 'learn',
#         'password': 'python'
#     }
# }

PLANETS = ['Mercury', 'Venus', 'Earth', 'Mars', 'Saturn', 'Jupiter', 'Uranus', 'Neptune']
regexp = r'\w+'
regexp_compile = re.compile(regexp)


def get_user_planets(user_text):
    """
    функция собирает в список все планеты указанные пользователем в запросе
    :param user_text:
    :return:
    """
    # user_text = user_text.split(', ')
    user_text = regexp_compile.findall(user_text)
    user_text = [word.capitalize() for word in user_text]

    user_planets = []
    for word in user_text:
        if word in PLANETS:
            user_planets.append(word)
    return user_planets


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planet(update, context):
    print('Вызван /planet')
    user_text = update.message.text
    tomorrow = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y/%m/%d')

    user_planets = get_user_planets(user_text)
    answer = []
    for planet in user_planets:

        if planet == 'Mercury':
            constellation = ephem.constellation(ephem.Mercury(tomorrow))
        elif planet == 'Venus':
            constellation = ephem.constellation(ephem.Venus(tomorrow))
        elif planet == 'Earth':
            constellation = ephem.constellation(ephem.Earth(tomorrow)) # Земли походу нет?
        elif planet == 'Mars':
            constellation = ephem.constellation(ephem.Mars(tomorrow))
        elif planet == 'Jupiter':
            constellation = ephem.constellation(ephem.Jupiter(tomorrow))
        elif planet == 'Saturn':
            constellation = ephem.constellation(ephem.Saturn(tomorrow))
        elif planet == 'Uranus':
            constellation = ephem.constellation(ephem.Uranus(tomorrow))
        elif planet == 'Neptune':
            constellation = ephem.constellation(ephem.Neptune(tomorrow))
        else:
            constellation = ['no data!']
        answer = f'Planet {planet}: ' + ', '.join(constellation)
        update.message.reply_text(answer)


def main():
    mybot = Updater(TOKEN, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
