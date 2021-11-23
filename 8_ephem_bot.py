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

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename='bot.log')


def greet_user(update, context):
	# getting user tg name
	user_name = list()
	chat_data = update['message']['chat']
	if chat_data['first_name']:
		user_name.append(chat_data['first_name'])
	if chat_data['last_name']:
		user_name.append(chat_data['last_name'])
	user_name = ' '.join(user_name) if user_name else 'пользователь'
	logging.info(f"Получен /start от {user_name}")
	update.message.reply_text(f'Привет, {user_name}! Ты вызвал команду /start')


def talk_to_me(update, context):
	user_text = update.message.text
	logging.info("Получено " + user_text)
	update.message.reply_text(user_text)


def planet_constellation(update, context):
	user_text = update.message.text
	logging.info("Получено " + user_text)
	user_text = user_text.split()
	if len(user_text) == 2:
		planet = None # avoid reference before assignment err
		planet_name = user_text[1].lower().capitalize()
		if planet_name == 'Mercury':
			planet = ephem.Mercury()
		elif planet_name == 'Venus':
			planet = ephem.Venus()
		elif planet_name == 'Mars':
			planet = ephem.Mars()
		elif planet_name == 'Jupiter':
			planet = ephem.Jupiter()
		elif planet_name == 'Saturn':
			planet = ephem.Saturn()
		elif planet_name == 'Neptune':
			planet = ephem.Neptune()
		elif planet_name == 'Uranus':
			planet = ephem.Uranus()
		elif planet_name == 'Pluto':
			planet = ephem.Pluto()
		else:
			update.message.reply_text('Не знаю такой планеты')
		planet.compute()
		const = ephem.constellation(planet)[1]
		update.message.reply_text(f'Планета {planet_name} находится сегодня в созвездии {const}')
	else:
		update.message.reply_text('Введи: /planet Planetname')

def main():
	mybot = Updater('BOTHFATHER_BOT_TOKEN', use_context=True)
	dp = mybot.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	dp.add_handler(CommandHandler("planet", planet_constellation))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))

	logging.info("Бот стартовал")

	mybot.start_polling()
	mybot.idle()


if __name__ == "__main__":
	main()
