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
                    filename='bot.log')


PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
  }


def greet_user(update, context):
    print("Вызван /start")
    #print(update)
    update.message.reply_text("Привет! Ты вызвал команду /start. Давай начнем!")


def talk_to_me(update, context):
    user_text = update.message.text
    print("Пользователь ввел: ", user_text)
    update.message.reply_text(user_text)


def planet_constellation(update, context):   
    user_text = update.message.text.split()
    user_body = user_text[1].lower().capitalize()
    
    body_class = getattr(ephem, user_body, None)
    if body_class:
        body = body_class('2021/11/26')                                 
        constellation = ephem.constellation(body)
        update.message.reply_text(constellation)
    else:
        update.message.reply_text(f'Объект с названием {user_body} не найден')


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot started")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
