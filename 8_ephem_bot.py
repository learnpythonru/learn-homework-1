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
                    filename=('foxysnow_bot'))



def get_planet(update, context):
    user_text = update.message.text
    print("Команда: " + user_text)

    planet_name = user_text.split(' ')[1]
    print(planet_name)

    planet = ''
    if planet_name == 'Moon':
      planet = ephem.Moon('2020/01/31')

    if planet_name == 'Mars':
      planet = ephem.Mars('2020/01/31')

    if planet_name == 'Saturn':
      planet = ephem.Saturn('2020/01/31')

    if planet_name == 'Venus':
      planet = ephem.Venus('2020/01/31')

    if planet_name == 'Pluto':
      planet = ephem.Pluto('2020/01/31')

    if planet_name == 'Jupiter':
      planet = ephem.Jupiter('2020/01/31')

    if planet:
      const = ephem.constellation(planet)
      update.message.reply_text(f'Планета {planet_name} находится в созвездии {const}')
    else:
      update.message.reply_text('Повторите запрос позднее')


def greet_user(update, context):
    text = 'Вызван /start'
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    update.message.reply_text("Повторюшка: " + user_text)


def main():
    mybot = Updater("1496717731:AAFCYx_KGLUCQAf_q0QRJFrKnKIbL51Iqug", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
