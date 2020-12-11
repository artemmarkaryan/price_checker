import telebot
import config

the_bot = telebot.TeleBot(
    token=config.BOT_TOKEN,
    parse_mode='html'
)

notification_bot = telebot.TeleBot(
    token=config.BOT_TOKEN,
    parse_mode='html'
)
