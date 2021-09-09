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
from datetime import datetime
import ephem
import settings


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


# PROXY = {
#     'proxy_url': settings.PROXY_url,
#     'urllib3_proxy_kwargs': {
#         'username': settings.PROXY_username,
#         'password': settings.PROXY_pass
#     }
# }


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def planet_constellation(update, context):
    user_text = update.message.text
    planet = user_text.split(' ')[1]
    date = datetime.now().date()
    ephem_planet = getattr(ephem, planet)(date)
    const = ephem.constellation(ephem_planet)
    print(const)
    update.message.reply_text(f'Сегодня {planet} находится в созвездии {const[1]}.')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text('Пожалуйста используйте команду: /planet (any planet)')


def main():
    mybot = Updater(settings.API_KEY, use_context=True)# request_kwargs=PROXY

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
