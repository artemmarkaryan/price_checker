import config
from bot.bot import the_bot
from bot.handlers import *
import logging
import engine

logging.basicConfig(level=logging.INFO)

engine.tests.EngineTest().test_url_match()
engine.parsers.tests.ParserTests().test_parsers()

the_bot.polling()
