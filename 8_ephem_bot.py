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
    
def planet_info(update, context):
    planets ={
        'Mars': ephem.Mars(),
        'Mercury': ephem.Mercury(),
        'Venus': ephem.Venus(),
        'Jupiter': ephem.Jupiter(),
        'Saturn': ephem.Saturn(),
        'Uranus': ephem.Uranus(),
        'Neptune': ephem.Neptune(),
        'Pluto': ephem.Pluto()
    }

    user_input = update.message.text.split()
    if len(user_input) != 2:
        update.message.reply_text('Введите команду в формате /planet Название_планеты')
        return
    
    planet_name = user_input[1].capitalize()
    if planet_name not in planets:
        update.message.reply_text('Я не знаю такую планету')
        return
    
    planet = planets[planet_name]
    planet.compute()
    constellation = ephem.constellation(planet)[1]
    update.message.reply_text(f'Планета {planet_name} сегодня в созвездии {constellation}')

def main():
    mybot = Updater('TOKEN', use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_info))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

