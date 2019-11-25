"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора elif и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import os
import logging
import ephem
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
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
    update.message.reply_text('Привет я Ehpem_bot')
    update.message.reply_text('Хотите узнать в каком созвездии находиться планета в данный момент ? Введите /planet и название планеты'
                              '\nна английском. (Например /planet Mars)')

def planet_constellation(bot, update):
    text = update.message.text.split(' ')
    today = datetime.datetime.today().strftime('%Y/%m/%d')
    text = text[1].lower()
    
    if text == 'mars':  # Сделал, как в ТЗ, но как по мне if многовато))
        position = ephem.Mars(today)
        constellation = ephem.constellation(position)
        update.message.reply_text(f'Планета {text} находится в созвездии {constellation}')
    elif text == 'moon':
        position = ephem.Moon(today)
        constellation = ephem.constellation(position)
        update.message.reply_text(f'Планета {text} находится в созвездии {constellation}')
    elif text == 'mercury':
        position = ephem.Mercury(today)
        constellation = ephem.constellation(position)
        update.message.reply_text(f'Планета {text} находится в созвездии {constellation}')
    elif text == 'venus':
        position = ephem.Venus(today)
        constellation = ephem.constellation(position)
        update.message.reply_text(f'Планета {text} находится в созвездии {constellation}')
    elif text == 'jupiter':
        position = ephem.Jupiter(today)
        constellation = ephem.constellation(position)
        update.message.reply_text(f'Планета {text} находится в созвездии {constellation}')
    elif text == 'saturn':
        position = ephem.Saturn(today)
        constellation = ephem.constellation(position)
        update.message.reply_text(f'Планета {text} находится в созвездии {constellation}')
    elif text == 'uranus':
        position = ephem.Uranus(today)
        constellation = ephem.constellation(position)
        update.message.reply_text(f'Планета {text} находится в созвездии {constellation}')
    elif text == 'neptune':
        position = ephem.Neptune(today)
        constellation = ephem.constellation(position)
        update.message.reply_text(f'Планета {text} находится в созвездии {constellation}')
    elif text == 'pluto':
        position = ephem.Pluto(today)
        constellation = ephem.constellation(position)
        update.message.reply_text(f'Планета {text} находится в созвездии {constellation}')    
    else:
        update.message.reply_text('Что-то пошло не так, попробуй название планеты на английском.')


def talk_to_me(bot, update):
    user_text = update.message.text 
    update.message.reply_text(user_text)
 

def main():
    mybot = Updater(os.environ.get("TELEGRAM_TOKEN"), request_kwargs=PROXY)
    
    logging.info('Bot is running')
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
    

if __name__ == "__main__":
    main()
