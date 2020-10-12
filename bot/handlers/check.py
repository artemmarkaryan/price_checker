from bot.bot import the_bot
from telebot.types import Message
from engine.match import match_parser_by_url
from engine.errors import UrlNotSupported
from database import facade
import logging


def handle_add(m: Message):
    the_bot.send_message(m.chat.id, 'Пришлите ссылку на товар')
    the_bot.register_next_step_handler(m, handle_url)


def handle_url(m: Message):
    if len(m.text.split()) > 1:
        the_bot.send_message(m.chat.id, 'Это не ссылка')
        handle_add(m)
        return

    url = m.text
    try:
        parser = match_parser_by_url(url)
        check = facade.check.add_check(m.chat.id, parser, url)
        the_bot.send_message(
            m.chat.id,
            f'Цена: {check.price_verbose}\nТеперь ссылка отслеживается'
        )
    except UrlNotSupported:
        handle_add(m)
