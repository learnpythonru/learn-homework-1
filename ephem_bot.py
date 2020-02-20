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
import settings
import ephem
import arrow

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


def body(bot, update):

    try:
        bodies_list = [x[-1] for x in ephem._libastro.builtin_planets()]
        p = update.message.text
        body_name = p.split(' ')[-1]
        date = str(arrow.now().date()).replace('-','/')
        calc_data = getattr(ephem, body_name)(date)
        final = ephem.constellation(calc_data)
        while True:
            for x in bodies_list:
                if x.replace("'","") == body_name:
                    update.message.reply_text(f"Планета находится в созвездии {final}")
                    return False
    except AttributeError:
        update.message.reply_text("Повторите название планеты.")



def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", body))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
