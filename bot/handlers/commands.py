from bot.bot import bot
from telebot.types import Message


@bot.message_handler(commands=['help'])
def handle_help(m: Message):
    bot.send_message(m.chat.id)