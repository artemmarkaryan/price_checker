from telegram.states.interface import TgStateInterface
from helpers import kb_generator
from engine import api
import config


class AddState(TgStateInterface):
    name = 'add'

    predefined_states = {
        config.KbButtons.CANCEL: 'initial'
    }

    def process_request(self, request):
        self.bot.send_message(
            request.chat.id,
            'А можно ссылочку на товар, пожалуйста\n🥺👉👈',
            reply_markup=kb_generator.generate_cancel()
        )

    def handle(self, response) -> str:
        added = api.add_link('telegram', response.chat.id, response.text)
        if added:
            return 'good_link'
        else:
            return 'bad_link'


class GoodLinkState(TgStateInterface):
    name = 'good_link'
    instant_next = 'initial'

    def process_request(self, request):
        self.bot.send_message(request.chat.id, 'Дело в шляпе 🤩\nТеперь можешь спать спокойно. Если вдруг цена изменится — я сразу дам знать')


class BadLinkState(TgStateInterface):
    name = 'bad_link'
    instant_next = 'add'

    def process_request(self, request):
        self.bot.send_message(request.chat.id, 'Да блин, такую ссылку я добавить не могу, сорян 😢')
