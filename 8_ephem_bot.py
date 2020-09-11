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
import settings

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
planets = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)


def planet_star(bot, update):
    print('planet_star function initialized')
    t = update.message
    var = update.message.text
    plnt = var.split() 

    if plnt[1].lower() == "mercury" or plnt[1].lower() == "меркурий":
      i = ephem.Mercury(t['date'])
      const = ephem.constellation(i)
      
    elif plnt[1].lower() == "venus" or plnt[1].lower() == "венера":
      i = ephem.Venus(t['date'])
      const = ephem.constellation(i)
      
    elif plnt[1].lower() == "mars" or plnt[1].lower() == "марс":
      i = ephem.Mars(t['date'])
      const = ephem.constellation(i)
      
    elif plnt[1].lower() == "jupiter" or plnt[1].lower() == "юпитер":
      i = ephem.Jupiter(t['date'])
      const = ephem.constellation(i)
      
    elif plnt[1].lower() == "saturn" or plnt[1].lower() == "сатурн":
      i = ephem.Saturn(t['date'])
      const = ephem.constellation(i)
      
    elif plnt[1].lower() == "neptune" or plnt[1].lower() == "нептун":
      i = ephem.Neptune(t['date'])
      const = ephem.constellation(i)
      
    elif plnt[1].lower() == "pluto" or plnt[1].lower() == 'плутон':
      i = ephem.Pluto(t['date'])
      const = ephem.constellation(i)

    elif plnt[1].lower() == "earth" or plnt[1].lower() == 'земля':
      update.message.reply_text('Про Землю ничего не знаю(')

    else:
      update.message.reply_text("Это не планета солнечной системы")
    update.message.reply_text(const)
    

def main():
    mybot = Updater(settings.api_key, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_star))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
