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
import ephem
import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
    'username': settings.PROXY_USERNAME,
    'password': settings.PROXY_PASSWORD
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)

dt_now = datetime.now()
today_d = (str(dt_now))[:10].replace("-","/")

def my_planet(pl_name, date_i):
    if pl_name == ephem.Mars().name:
        m = ephem.Mars(date_i)
        return ephem.constellation(m)
    elif pl_name == ephem.Venus().name:
        m = ephem.Venus(date_i)
        return ephem.constellation(m)
    elif pl_name == ephem.Mars().name:
        m = ephem.Mars(date_i)
        return ephem.constellation(m)
    elif pl_name == ephem.Jupiter().name:
        m = ephem.Jupiter(date_i)
        return ephem.constellation(m)
    elif pl_name == ephem.Saturn().name:
        m = ephem.Saturn(date_i)
        return ephem.constellation(m)
    elif pl_name == ephem.Uranus().name:
        m = ephem.Uranus(date_i)
        return ephem.constellation(m)
    elif pl_name == ephem.Neptune().name:
        m = ephem.Neptune(date_i)
        return ephem.constellation(m)
    else:
        return "I don't know your planet, sorry. Enter another planet name."



def planet_info(update, context):
    print(context.args)
    if context.args:
        try:
            user_planet = (context.args[0])
            message = f'Planet {context.args[0]} is in {my_planet(user_planet, today_d)[1]} constellation today.'
        except (TypeError, ValueError):
            message = "Enter a name of planet in the solar sistem after '/planet"
    else:
        message = "Enter a name of planet in the solar sistem after '/planet"
    update.message.reply_text(message)
#-remove-------below






def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_info))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
