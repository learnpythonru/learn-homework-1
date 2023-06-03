import ephem
from glob import glob
from datetime import date
from random import choice
from utils import get_smile, main_keyboard, play_random_game
from settings import IMG_PATH


def greet_user(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f'Привет, {update["message"]["chat"]["first_name"]}! {context.user_data["emoji"]}',
                              reply_markup=main_keyboard())


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text,
                              reply_markup=main_keyboard())


def constellation_planet(update, context):
    planets_name = {
        'mars': ephem.Mars,
        'mercury': ephem.Mercury,
        'venus': ephem.Venus,
        'jupiter': ephem.Jupiter,
        'saturn': ephem.Saturn,
        'uranus': ephem.Uranus,
        'neptune': ephem.Neptune
    }
    planet = update.message.text.split()[1].lower()
    con_planet = ephem.constellation(planets_name[planet](date.today()))

    if planet in planets_name:
        update.message.reply_text(
            f'Планета {planet.capitalize()} находится в созведии {con_planet[1]} ({con_planet[0]})',
            reply_markup=main_keyboard()
        )


def guess_number(update, context):
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_game(user_number)
        except (TypeError, ValueError):
            message = 'Введите целое число'
    else:
        message = 'Введите число'
    update.message.reply_text(message,
                              reply_markup=main_keyboard())


def choice_logo(update, context):
    logos_path = glob(fr'{IMG_PATH}\logo*.jp*g')
    logo_photos = choice(logos_path)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id, photo=open(logo_photos, 'rb'),
                           reply_markup=main_keyboard())


def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(f'Ваши координаты: {coords} {context.user_data["emoji"]}', reply_markup=main_keyboard())
    print(f'{update.message.location} user: {update["message"]["chat"]["first_name"]}')
