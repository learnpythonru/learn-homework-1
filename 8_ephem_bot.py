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

TOKEN = None
user_planet = None

with open("token.txt") as f:
    TOKEN = f.read().strip()

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
 
def get_planet(bot, update):
    user_text = update.message.text
    user_planet = user_text.split()[1]
    print(f"user_planet: {user_planet}")

    if user_planet == "Mars":
        whereis_planet = ephem.Mars(ephem.now())
    elif user_planet == "Jupiter":
        whereis_planet = ephem.Jupiter(ephem.now())
    elif user_planet == "Saturn":
        whereis_planet = ephem.Saturn(ephem.now())
    elif user_planet == "Uranus":
        whereis_planet = ephem.Uranus(ephem.now())
    else:
        whereis_planet = None

    print(f"whereis_planet: {whereis_planet}")
    if whereis_planet:
        constellation = ephem.constellation(whereis_planet)
        print(constellation)
        update.message.reply_text(f"{user_planet} is in {constellation[1]}") 
    else:
        print("Unknown planet")
        update.message.reply_text("Unknown planet") 

def main():
    mybot = Updater(TOKEN, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
