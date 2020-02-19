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
import logging, bot_settings, datetime, ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)

def greet_user(bot, update):
    planet_list = [name for _0, _1, name in ephem._libastro.builtin_planets()]
    text = 'Привет. Для получения данных о фазах луны введи /planet и название планеты со ' \
           'списка %s без кавычек для проверки созвездия. Пример /planet Mars' % planet_list
    print(text)
    update.message.reply_text(text)


def choose_planet(bot, update):
    planet_list = [name for _0, _1, name in ephem._libastro.builtin_planets()]
    text = update.message.text
    planet_name = text.split(" ")[1]
    curent_date = datetime.datetime.now().strftime("%Y/%m/%d")
    planet_data = getattr(ephem,planet_name)(curent_date)
    position = ephem.constellation(planet_data)
    while True:
        for key in planet_list:
            if key == planet_name:
                update.message.reply_text(f"Сегодня планета {planet_name} находиться в созвездии {position}")
                return False
        else:
            print("Я не понимаю о чем ты, спроси что нибудь о другом")
            return greet_user()


    # update.message.reply_text(f"")


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 

def main():
    mybot = Updater(bot_settings.TELEGRAM_API_KEY, request_kwargs=bot_settings.PROXY, use_context=False)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", choose_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
