from bot.bot import the_bot
from bot.handlers import *
import logging
import engine
import threading as th


logging.getLogger().setLevel(logging.INFO)
logging.info('starting')

engine.tests.EngineTest().test_url_match()
engine.parsers.tests.ParserTests().test_parsers()

bot_polling_p = th.Thread(
    target=the_bot.polling,
    kwargs={
        'interval': 0.1,
        'none_stop': False
    },
    daemon=True)
price_tracking_p = th.Timer(
    interval=60,
    function=engine.tracker.execute,
)

price_tracking_p.start()
bot_polling_p.start()

while True:
    pass
