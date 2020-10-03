from bot.bot import the_bot
from telebot.types import Message
from engine.match import match_parser
from engine.errors import UrlNotSupported
from db_interface import interfaces
import logging


def handle_add(m: Message):
    the_bot.send_message(m.chat.id, 'Пришлите ссылку на товар')
    the_bot.register_next_step_handler(m, handle_url)


def handle_url(m: Message):
    url = m.text
    try:
        parser = match_parser(url)
        check = interfaces.check.add_check(m.chat.id, parser, url)
        the_bot.send_message(
            m.chat.id,
            f'Цена: {check.price_verbose}\nТеперь ссылка отслеживается'
        )
    except UrlNotSupported:
        handle_add(m)
