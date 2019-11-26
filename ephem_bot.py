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
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 
#mars = ephem.Mars('2000/01/01')
#const = ephem.constellation(mars)
#print(const)

def planet_stars(bot, update):
    user_planet = update.message.text.split(" ")[1]
    print("Вы выбрали: ", user_planet)
    date = datetime.datetime.now()
    date = date.strftime("%Y/%m/%d")
    print(type(date))
    print("Сегодня ", date)

    planets = {
        "Mercury":  ephem.Mercury(date),
        "Venus":    ephem.Venus(date),
        "Mars":     ephem.Mars(date),
        "Jupiter":  ephem.Jupiter(date),
        "Saturn":   ephem.Saturn(date),
        "Uranus":   ephem.Uranus(date),
        "Neptune":  ephem.Neptune(date),
    }
    for key, value in planets.items():
        if key == user_planet:
            const = ephem.constellation(value)
            print(key, "в" , const[1])
            update.message.reply_text(f'{key} в {const[1]}')

def main():
    mybot = Updater("876514281:AAHTzSbR8O8Whd6fCOScpnwar31dEDzacWM", request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_stars))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
