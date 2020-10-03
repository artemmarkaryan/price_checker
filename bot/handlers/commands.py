from bot.bot import bot
from db_interface.interfaces import texts
from db_interface.errors import *
from telebot.types import Message


@bot.message_handler(commands=['help'])
def handle_help(m: Message):
    try:
        help_text: str = texts.get(name='info')
        bot.send_message(m.chat.id, help_text)
    except TooManyValues or DoesNotExist:
        pass
        # todo: notify admin about errors
