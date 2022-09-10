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
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

planet_dict = {'Mars': ephem.Mars(date.today()), 'Venus': ephem.Venus(date.today()), 'Saturn': ephem.Saturn(date.today()), 'Jupiter': ephem.Jupiter(date.today()),
               'Neptune': ephem.Neptune(date.today()), 'Uranus': ephem.Uranus(date.today()), 'Mercury': ephem.Mercury(date.today())}
def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def planets(update, context):
    planetname = update.message.text.split()[1]
    isplanet = planet_dict.get(planetname, None)
    if isplanet != None:
        constellation = ephem.constellation(planet_dict[planetname])
        update.message.reply_text(constellation[1])
        update.message.reply_text('Такой планеты нет')


    


def main():
    mybot = Updater("5437432503:AAFHarbS1qyUzjB4cAkmma2VBDsMfPnzHso", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planets))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
