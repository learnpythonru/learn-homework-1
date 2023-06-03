from random import randint, choice
from settings import USER_EMOJI
from telegram import ReplyKeyboardMarkup, KeyboardButton
from emoji import emojize


def play_random_game(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f'Ваше число {user_number}, мое {bot_number}. Вы выиграли!'
    elif user_number == bot_number:
        message = f'Ваше число {user_number}, мое {bot_number}. У нас ничья'
    else:
        message = f'Ваше число {user_number}, мое {bot_number}. Вы проиграли('
    return message


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(USER_EMOJI)
        return emojize(smile, language='alias')
    return user_data['emoji']


def main_keyboard():
    return ReplyKeyboardMarkup([['Отправить лого', KeyboardButton('Мои координаты', request_location=True)],
                                ['Еще не придумал', 'Еще не придумал']])
