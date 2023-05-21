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

  mercury,     venus,     mars, jupiter,     saturn,      uranus,
    neptune,     pluto,     sun,     moon
"""
import logging
import settings as settings
import ephem
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename="bot.log", level=logging.INFO)

def planet_in_constellation_v2(planet:str)->str:
    planets = ['mercury', 'venus', 'mars', 'jupiter', 'saturn',
                'uranus', 'neptune', 'pluto', 'sun', 'moon']
    if planet.lower() in planets:
        e_planet = getattr(ephem, f'{planet.capitalize()}')
        return ephem.constellation(e_planet(datetime.today()))[1]
    


def planet_in_constellation(planet:str)->str:
    match planet.lower():
        case "mercury":  
            return ephem.constellation(ephem.Mercury(datetime.today()))[1]
        case "venus":  
            return ephem.constellation(ephem.Venus(datetime.today()))[1]
        case "mars":  
            return ephem.constellation(ephem.Mars(datetime.today()))[1]
        case "jupiter":  
            return ephem.constellation(ephem.Jupiter(datetime.today()))[1]
        case "saturn":  
            return ephem.constellation(ephem.Saturn(datetime.today()))[1]
        case "uranus":  
            return ephem.constellation(ephem.Uranus(datetime.today()))[1]
        case "neptune":  
            return ephem.constellation(ephem.Neptune(datetime.today()))[1]
        case "pluto":  
            return ephem.constellation(ephem.Pluto(datetime.today()))[1]
        case "sun":  
            return ephem.constellation(ephem.Sun(datetime.today()))[1]
        case "moon":  
            return ephem.constellation(ephem.Moon(datetime.today()))[1]
        case _:
            return "O_O"


def planet_constellation(update, context):
    message_text = update.message.text.split()[1].lower()
   # print(message_text)
   #print(str(message_text).lower())
    if message_text in ['mercury', "venus", "mars", "jupiter", "saturn", "uranus",  "neptune", "pluto", "sun", "moon"]:
        update.message.reply_text(message_text.capitalize() + " in " + planet_in_constellation_v2(message_text))
    else:
        update.message.reply_text("Попробуйте \n /planet Mercury \n /planet Venus \n /planet Mars \
                                  \n /planet Jupiter \n /planet Saturn \n /planet Uranus \n /planet Neptune \
                                  \n /planet Pluto")


def greet_user(update, context):
    print("update", update)
    print(context)
    print('Жмак старт')
    update.message.reply_text("q123")


def talk_to_me(update, context):
    text = update.message.text
    user = update.message.chat.username
    print(user, text)
    update.message.reply_text( user + ":" + text)



def main():
    mybot = Updater(settings.API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

  #  print(planet_in_constellation("SUN"))


#    logging.info('Старт бота')

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
    