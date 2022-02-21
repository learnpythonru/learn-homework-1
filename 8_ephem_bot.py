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


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}

date_planet = '2000/01/10'

planet_names = {'Mercury': ephem.Mercury(date_planet),
                'Venus': ephem.Venus(date_planet),
                'Mars': ephem.Mars(date_planet),
                'Jupiter': ephem.Jupiter(date_planet),
                'Saturn': ephem.Saturn(date_planet),
                'Uranus': ephem.Uranus(date_planet),
                'Neptune': ephem.Neptune(date_planet),
                'Pluto': ephem.Pluto(date_planet)
                }


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользаватель!')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def constellation_planet(update, context):
    user_planet = update.message.text.split()[1]
    if user_planet in planet_names:
        ephem_planet = planet_names.get(user_planet, None)
        constellation = ephem.constellation(ephem_planet)
        update.message.reply_text(constellation)
    else:
        update.message.reply_text('Неизвестная планета')


def main():
    mybot = Updater("5127408752:AAHyqNdZ8Ur8JaBuT4zPptxboh127PBDq64",
                    request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", constellation_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
