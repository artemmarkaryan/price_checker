from bot.bot import the_bot
from bot.handlers import *
import logging
import engine
import threading as th

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    engine.tests.EngineTest().test_url_match()
    engine.parsers.tests.ParserTests().test_parsers()

    bot_polling_p = th.Thread(target=the_bot.polling, daemon=True)
    price_tracking_p = th.Thread(target=engine.tracker.process, daemon=True)

    price_tracking_p.start()
    bot_polling_p.start()
    while True:
        pass
