from telebot.types import *
from config import KB_BUTTONS


def generate_inline(row_width=2, **variants):
    kb = InlineKeyboardMarkup(row_width=row_width)
    for k, v in variants:
        kb.add(InlineKeyboardButton(
            text=k, callback_data=v
        ))
    return kb


def generate_reply(row_width, *variants):
    kb = ReplyKeyboardMarkup(
        row_width=1, resize_keyboard=True, one_time_keyboard=True
    )
    for v in variants:
        kb.add(v)
    return kb


def generate_cancel():
    kb = ReplyKeyboardMarkup(
        row_width=1, resize_keyboard=True, one_time_keyboard=True
    )
    kb.add(KB_BUTTONS['CANCEL'])
    return kb

