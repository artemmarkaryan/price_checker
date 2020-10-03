from bot.bot import the_bot
from db_interface.interfaces import *
from db_interface.errors import *
from bot.handlers import check
from telebot.types import Message


@the_bot.message_handler(commands=['start'])
def handle_start(m: Message):
    user.get_or_create(m.chat.id)
    handle_help(m)


@the_bot.message_handler(commands=['help'])
def handle_help(m: Message):
    try:
        help_text: str = text.get(name='help')
        the_bot.send_message(m.chat.id, help_text)
    except TooManyValues or DoesNotExist:
        pass
        # todo: notify admin about errors


@the_bot.message_handler(commands=['add'])
def handle_add_check(m: Message):
    check.handle_add(m)
