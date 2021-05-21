import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
from datetime import datetime


PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    
    print("Вызван /start")
    update.message.reply_text("Hello usver!")

def talk_to_me(update, context):
    
    # Эхо-ответы от бота
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def get_constellation(update, context):
   
    print("Вызван /planet")
    text = update.message.text.split()
    if len(text) != 2:
        update.message.reply_text('Введите запрос в формате: /planet "имя планеты".') 
    request, planet = text
    try:
        date = datetime.now().date()
        set_planet = getattr(ephem, planet)
        mars = set_planet(date)
        update.message.reply_text(ephem.constellation(mars))
    except AttributeError:
        update.message.reply_text('Такой планеты нет в списке.')
    

def main():
    
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
  # dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation))
 #  dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Bot starting!")
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

if __name__ == '__main__':
    main()