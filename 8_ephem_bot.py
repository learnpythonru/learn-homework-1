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
# Импортируем нужные компоненты
import logging, ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

# Настройки прокси
PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Я пока еще ничего не умею, но могу сказать, что ты только что вызвал команду /start')

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def planets(update, context):
    # mars = ephem.Mars('2021/03/03')
    # const = ephem.constellation(mars)
    # print(const)
    planet_name = str(update.message.text.split()[1]).lower().capitalize()

    day = date.today().split("-")
    print(day)

    print(planet_name)
    update.message.reply_text(planet_name)

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planets))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")

    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()


# Вызываем функцию main() - именно эта строчка запускает бота
if __name__ == "__main__":
    main()
