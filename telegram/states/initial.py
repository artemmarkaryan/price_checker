from telegram.states.interface import TgStateInterface
from helpers import kb_generator
from config import KbButtons


class InitialState(TgStateInterface):
    name = 'initial'
    predefined_states = {
        KbButtons.ADD: 'add',
    }

    def process_request(self, request):
        self.bot.send_message(
            request.chat.id,
            'Ну чем займёмся? 👀',
            reply_markup=kb_generator.generate_reply(
                KbButtons.ADD
            )
        )
