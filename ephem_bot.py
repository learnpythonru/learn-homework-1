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
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import random
import ephem
import settings
from datetime import datetime


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        filename='bot.log'
        ) 

def talk_to_me(bot, update):
    upc = update.message.chat
    word_from_user = update.message.text
    break_word = ''.join([random.choice(['?','*','@', '%', '<', '>', '!', '$']) if i%2 else v for i,v in enumerate(word_from_user)])

    if len(word_from_user) > 5: 
        update.message.reply_text(f'{break_word}  <----  \\~.~/\nслишком много букав, я еще так молод, чтобы это понять!')
    else:
        update.message.reply_text(f'Что, что ты сказал? Мне показалось или это было:\n{word_from_user}')
    logging.info(f'User: {upc.username}, Chat id: {upc.id}, Message:{update.message.text}')


def greet_user(bot, update):
    upc = update.message.chat

    if upc.last_name:
        u_name = f'{upc.first_name} {upc.last_name}'
    else:
        u_name = f'{upc.first_name}'

    text = f'Я бот, а ты - @{upc.username} , по имени {u_name}'

    update.message.reply_text(text)
    bot.send_photo(chat_id=upc.id, photo=open('img/hi.jpg', 'rb'))



def planet_naming(bot, update):
    current_time = datetime.now().strftime('%Y/%m/%d')
    planet = ''.join(update.message.text.split()[1]).lower()
    const = 'i don\' know that planet'
    
    if planet == 'mars': const = ephem.constellation(ephem.Mars(current_time))[1]
    if planet == 'mercuy': const = ephem.constellation(ephem.Mercury(current_time))[1] 
    if planet == 'venus': const = ephem.constellation(ephem.Venus(current_time))[1] 
    if planet == 'jupiter': const = ephem.constellation(ephem.Jupiter(current_time))[1] 
    if planet == 'saturn': const = ephem.constellation(ephem.Saturn(current_time))[1]
    if planet == 'uranus': const = ephem.constellation(ephem.Uranus(current_time))[1] 
    if planet == 'neptune': const = ephem.constellation(ephem.Neptune(current_time))[1] 
    if planet == 'moon': const = ephem.constellation(ephem.Moon(current_time))[1]      

    update.message.reply_text(const)    


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    logging.info('Я проснулся')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet',planet_naming))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
