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
from turtle import update
import logging
import settings
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime

logging.basicConfig(filename="bot.log", level=logging.INFO)

ephem_built_in_planets = [name for _0, _1, name in ephem._libastro.builtin_planets()]

def planet_constellation_now(text):
    planet_name = text.replace("/planet ","")
    if planet_name in ephem_built_in_planets:
        return ephem.constellation(getattr(ephem, planet_name)(datetime.datetime.now()))[1]


def help(update, context):
    update.message.reply_text("Напиши /planet название планеты, что бы узнать в каком созвездии сегодня находится планета\n\nДля того что бы получить список доступных планет напиши /all_planet")

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Доброго здоровьица мой дорогой.\nНапиши /planet название планеты, что бы узнать в каком созвездии сегодня находится планета\n\n Для того что бы получить список доступных планет напиши /all_planet \n\nЕсли запутался ты всегда можешь вызвать команду /help")

def all_planet(update, context):
    update.message.reply_text(ephem_built_in_planets)


def talk_to_me(update, context):
    text = update.message.text
    logging.info(text)
    if text.split(" ")[0] == "/planet":
        update.message.reply_text(f"Планета находится в созвездии {planet_constellation_now(text)}")
     
def main():
    #Создаем бот и передаем ему ключ для авторизации
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    
    dp.add_handler(CommandHandler("all_planet", all_planet))
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()

    mybot.idle()

if __name__ == '__main__':
    main()
