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
import numexpr as ne
from random import randint
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date, datetime
from settings import TOKEN, PROXY

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

date_now = date.today()


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def in_which_constellation(update, context):
    user_text = update.message.text.split()[1].capitalize()
    planet = getattr(ephem, user_text)
    constellation = ephem.constellation(planet(date_now))[1]
    update.message.reply_text(f'Планета {user_text} в созвездии {constellation}')


def next_full_moon(update, context):
    try:
        user_text = update.message.text.split()[1]
        user_date = datetime.strptime(user_text, '%Y-%m-%d')
        update.message.reply_text(f'Следующее полнолуние {ephem.next_full_moon(user_date)}')
    except IndexError:
        update.message.reply_text(f'Следующее полнолуние {ephem.next_full_moon(date_now)}')


def calculate(update, context):
    user_text = update.message.text.split(' ')
    str_expr = ''.join(user_text[1:])
    try:
        result = ne.evaluate(str_expr)
    except ZeroDivisionError:
        update.message.reply_text('Нельзя делить на ноль')
    update.message.reply_text(f'{result}')


def helper(update, context):
    update.message.reply_text('Команда /planet работает следующим образом\nНапример: /planet Jupiter\n'
                              'А так же: \nMars,\nMercury,\nMoon,\nNeptune, Pluto,'
                              '\nSaturn, Uranus, Venus, Jupiter')


def create_cities_list():
    with open('goroda.csv', 'r', encoding='utf-8') as f:
        li = []
        for i in f:
            li.append(i.split(',')[0])
        return li


cities_list = create_cities_list()
last_letter_bot_city = '0'


def cities(update, context):
    user_city = update.message.text.split()[1].capitalize()
    global last_letter_bot_city
    global cities_list
    if user_city.lower() == 'stop':
        cities_list = create_cities_list()
        last_letter_bot_city = '0'
        update.message.reply_text('Игра окончена!')
    elif (user_city in cities_list and user_city[0] == last_letter_bot_city.upper()) or last_letter_bot_city == '0':
        last_letter_user_city = user_city[-1]
        if last_letter_user_city == 'й':
            last_letter_user_city = 'и'
        elif last_letter_user_city in ['ь', 'ы']:
            last_letter_user_city = user_city[-2]
        # update.message.reply_text(f'Тебе на "{last_letter_bot_city.upper()}"')
        cities_list.remove(user_city)
        li_lit = []
        for i in cities_list:
            if i[0] == last_letter_user_city.upper():
                li_lit.append(i)
        print(li_lit)
        bot_city = li_lit[randint(0, len(li_lit))]
        update.message.reply_text(bot_city)
        last_letter_bot_city = bot_city[-1]
        if last_letter_bot_city == 'й':
            last_letter_bot_city = 'и'
        elif last_letter_bot_city in ['ь', 'ы']:
            last_letter_bot_city = bot_city[-2]
        update.message.reply_text(f'Тебе на "{last_letter_bot_city.upper()}"')
    else:
        update.message.reply_text(f'Неа, тебе на "{last_letter_bot_city.upper()}"')


def wordcount(update, context):
    user_text = update.message.text.split(' ')[1:]
    print(user_text)
    if not user_text:
        update.message.reply_text('это что такое? пустая строка? и что прикажешь считать?')
    else:
        update.message.reply_text(f'{len(user_text)} слова')
# /wordcount 1234567 2345678 @#$%ˆ&*  - подумать как сделать проверку


def main():
    mybot = Updater(TOKEN, request_kwargs=PROXY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", in_which_constellation))
    dp.add_handler(CommandHandler("help", helper))
    dp.add_handler(CommandHandler('wordcount', wordcount))
    dp.add_handler(CommandHandler('next_full_moon', next_full_moon))
    dp.add_handler(CommandHandler('cities', cities))
    dp.add_handler(CommandHandler('calc', calculate))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
