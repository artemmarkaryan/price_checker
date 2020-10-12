from bot.bot import the_bot
from typing import Dict


class StateInterface:
    bot = the_bot
    name = ''
    next_states: Dict[str, str] = dict()

    def send_message(self, user_id):
        ...

    def handler(self, message):
        print(get_subclasses())
        for message_text, class_name in self.next_states.items():
            if message.text == message_text:
                get_subclasses()[class_name].process_message(message)
                return

    def process_message(self, message):
        self.send_message(message.chat.id)
        self.bot.register_next_step_handler(
            message, self.handler
        )


def get_subclasses() -> Dict[str, StateInterface]:
    return {
        s.name: s() for s in StateInterface.__subclasses__()
    }
