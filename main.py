from bot.bot import the_bot
import logging
import engine
import threading as th
from bot import states

logging.getLogger().setLevel(logging.INFO)
logging.info('starting')


@the_bot.message_handler(func=lambda m: True)
def initial_handler(m):
    states.initial.InitialState().handler(m)


tests = (
    # engine.tests.EngineTest().test_url_match,
    # engine.parsers.tests.ParserTests().test_parsers
)

for test in tests:
    test()

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

# price_tracking_p.start()
bot_polling_p.start()

while True:
    pass
