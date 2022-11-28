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


def planet_search(update,context):
    planets=['солнце', 'луна', 'меркурий', 'венера', 'марс', 'сатурн', 'уран', 'нептун', 'юпитер',]
    user_text = update.message.text.split()[1].lower()
    print('поиск планеты...')
    print('планета, которую ввел пользователь', user_text)
    for planet in planets:
        if user_text == planet:
            if user_text == 'солнце':
                planet_answer = ephem.constellation(ephem.Sun(datetime.datetime.now().strftime('%Y')))
                update.message.reply_text(planet_answer)
            elif user_text == 'луна':
                planet_answer=ephem.constellation(ephem.Moon(datetime.datetime.now().strftime('%Y')))
                update.message.reply_text(planet_answer)
            elif user_text == 'меркурий':
                planet_answer=ephem.constellation(ephem.Mercury(datetime.datetime.now().strftime('%Y')))
                update.message.reply_text(planet_answer) 
            elif user_text == 'венера':
                planet_answer=ephem.constellation(ephem.Venus(datetime.datetime.now().strftime('%Y')))
                update.message.reply_text(planet_answer)
            elif user_text == 'марс':
                planet_answer=ephem.constellation(ephem.Mars(datetime.datetime.now().strftime('%Y')))
                update.message.reply_text(planet_answer)
            elif user_text == 'юпитер':
                planet_answer=ephem.constellation(ephem.Jupiter(datetime.datetime.now().strftime('%Y')))
                update.message.reply_text(planet_answer) 
            elif user_text == 'сатурн':
                planet_answer=ephem.constellation(ephem.Saturn(datetime.datetime.now().strftime('%Y')))
                update.message.reply_text(planet_answer)
            elif user_text == 'уран':
                planet_answer=ephem.constellation(ephem.Uranus(datetime.datetime.now().strftime('%Y')))
                update.message.reply_text(planet_answer)
            elif user_text == 'нептун':
                planet_answer=ephem.constellation(ephem.Neptune(datetime.datetime.now().strftime('%Y')))
                update.message.reply_text(planet_answer) 
            


def main():
    mybot = Updater("", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_search))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
