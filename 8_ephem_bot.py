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
import settings
import ephem
from difflib import get_close_matches
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from constellations import constellations

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

GREET_TEXT = '''Привет!
Напиши мне /planet и название планеты, а я скажу в каком она созвездии.
Или /help для вывода списка планет.'''

planets = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(GREET_TEXT)
     
def help(update, context):
    text = 'Вызван /help'
    print(text)
    update.message.reply_text('Планеты: ' + ', '.join(planets))

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(f'Вы написали {user_text}')

def planet(update, context):
    user_text = update.message.text.lower()
    user_data = user_text.split()
    if user_text == '/planet':
        update.message.reply_text('Напиши после команды через пробел название планеты. К примеру:')
        update.message.reply_text('/planet Mars')
    elif len(user_data) != 2:
        update.message.reply_text('Напиши после команды через пробел название ОДНОЙ планеты. К примеру:')
        update.message.reply_text('/planet Mars')
    else:
        planet = user_data[1].capitalize()
        if planet == 'Earth':
            update.message.reply_text('Мы сейчас на этой планете, не знал?)')
            return
        if planet == 'Moon':
            update.message.reply_text('Это спутник, а не планета, ну да ладно.')
            
        if planet != 'Moon' and planet not in planets:
            close_match = get_close_matches(planet, planets, n=1)
            if close_match:
                update.message.reply_text(f'Вероятно ты имел в виду {close_match[0]}, а не {planet}.')
                planet = close_match[0]
            else:
                update.message.reply_text(f'Нажми /help и зацени какие планеты доступны.')
                return
        body = getattr(ephem, planet)
        day = date.today()
        constellation = ephem.constellation(body(day))[1]
        constellation_rus, constellation_ukr = constellations[constellation]
        update.message.reply_text(f'{planet} в созвездии {constellation} ({constellation_rus}/{constellation_ukr}).')

def main():
    mybot = Updater(settings.token, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    print('Я работаю!')
    mybot.idle()


if __name__ == "__main__":
    main()
