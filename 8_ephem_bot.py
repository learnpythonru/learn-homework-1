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
# import logging
import ephem, datetime, settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)
    update.message.reply_text('Введите /planet и название планеты (Mercury, Venus, Mars, Jupiter, '
                              'Saturn, Uranus, Neptune)')


def talk_to_me(update, context):

    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def planet(update, context):

    date_now = datetime.datetime.now().strftime('%y/%m/%d')
    # date_now = ephem.now()
    user_text = update.message.text.split()[-1].capitalize()
    dict_planets = {'Mercury': ephem.Mercury,
                    'Venus': ephem.Venus,
                    'Mars': ephem.Mars,
                    'Jupiter': ephem.Jupiter,
                    'Saturn': ephem.Saturn,
                    'Uranus': ephem.Uranus,
                    'Neptune': ephem.Neptune}
    if user_text in dict_planets:
        constellation = ephem.constellation(dict_planets[user_text](date_now))
        print(constellation)
        update.message.reply_text(constellation)

    else:
        print('Введите /planet mars')
        update.message.reply_text(f'Введите "/planet {dict_planets}"')



def main():

    mybot = Updater(settings.API_KEY , use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
