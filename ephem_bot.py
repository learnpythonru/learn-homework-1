import datetime
import ephem
import logging

from glob import glob
from random import choice

from emoji import emojize
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}

API_KEY = "886440728:AAEWAxQ7haqJ3wjvQZJZe6Sv4Q2NUsLsC7Y"   

USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)

def greet_user(bot, update, user_data):
    emo = emojize(choice(settings.USER_EMOJI), use_aliases=True)
    user_data['emo'] = emo
    text = 'Привет {}'.format(emo)
    update.message.reply_text(text)

def talk_to_me(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, emo, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, update.message.chat.id, 
                        update.message.text)
    update.message.reply_text(user_text)

def get_const_planet(bot, update, user_data):
    planet = split(text)[1]
    print(text)
    print(planet)
    planets_list = [name for _0, _1, name in ephem._libastro.builtin_planets()]
    
    if planet in planets_list:
      pl = ephem.planet(now.strftime("%Y/%m/%d"))
      const = ephem.constellation(pl)
      print(const)
      update.message.reply_text(const)

def get_car_picture(bot, update, user_data):
    car_list = glob('images/*.jp*g')
    car_picture = choice(car_list)
    bot.send_photo(chat_id=update.message.chat.id, photo=open(car_picture, 'rb'))

def get_user_emo(user_data):
    if 'emo' in user_data:
        return user_data['emo']
    else:
        user_data['emo'] = emojize(choice(settings.USER_EMOJI), use_aliases=True)
        return user_data['emo']

def main():
    #learn1_axl_bot
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler("car", get_car_picture))
    dp.add_handler(CommandHandler("planet", get_const_planet))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       
main()

