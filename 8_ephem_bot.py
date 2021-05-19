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
import logging, settings, ephem
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

planets = ('Sun', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto')


PROXY = {
    'proxy_url': settings.PROXY_ULR,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}


def greet_user(update, context):
    text = 'Приветствую, на данный момент бод тестирует работу команды /planet'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def find_planet(update, context):
    global planets
    
    if context.args:

        inpt = context.args[0].title()
        print(inpt)

        
        if inpt == 'Sun':
            space_object = ephem.Sun(date.today())
            message = f'Вы выбрали планету "{inpt}". Эта планета находится в созвездии: {list(ephem.constellation(space_object))[1]}'

        elif inpt == 'Mercury':
            space_object = ephem.Mercury(date.today())
            message = f'Вы выбрали планету "{inpt}". Эта планета находится в созвездии: {list(ephem.constellation(space_object))[1]}'
                
        elif inpt == 'Venus':
            space_object = ephem.Venus(date.today())
            message = f'Вы выбрали планету "{inpt}". Эта планета находится в созвездии: {list(ephem.constellation(space_object))[1]}'

        elif inpt == 'Mars':
            space_object = ephem.Mars(date.today())
            message = f'Вы выбрали планету "{inpt}". Эта планета находится в созвездии: {list(ephem.constellation(space_object))[1]}'

        elif inpt == 'Jupiter':
            space_object = ephem.Jupiter(date.today())
            message = f'Вы выбрали планету "{inpt}". Эта планета находится в созвездии: {list(ephem.constellation(space_object))[1]}'

        elif inpt == 'Saturn':
            space_object = ephem.Saturn(date.today())
            message = f'Вы выбрали планету "{inpt}". Эта планета находится в созвездии: {list(ephem.constellation(space_object))[1]}'
                
        elif inpt == 'Uranus':
            space_object = ephem.Uranus(date.today())
            message = f'Вы выбрали планету "{inpt}". Эта планета находится в созвездии: {list(ephem.constellation(space_object))[1]}'

        elif inpt == 'Neptune':
            space_object = ephem.Neptune(date.today())
            message = f'Вы выбрали планету "{inpt}". Эта планета находится в созвездии: {list(ephem.constellation(space_object))[1]}'

        elif inpt == 'Pluto':
            space_object = ephem.Pluto(date.today())
            message = f'Вы выбрали планету "{inpt}". Эта планета находится в созвездии: {list(ephem.constellation(space_object))[1]}'

        else:
            message = f'Вы должны указать название планеты из списка:  {planets}'

    else:

        message = f'Вы должны указать название планеты из списка:  {planets}'
    

    print("Вызов /planet")
    
    update.message.reply_text(message)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", find_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
