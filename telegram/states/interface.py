from telebot.types import Message
from telegram.bot import the_bot
from typing import Dict
import logging


class TgStateInterface:
    """
    State gets users request, sends a unique message, than awaits users response.
    When got users response, state decides which state is next.
    Then state sends users response to the new state.
    New state treats the message as a request.
    """
    bot = the_bot
    name = ''
    universal_states = {
        '/add': 'add',
        '/start': 'initial',
        '/help': 'help',
    }
    predefined_states: Dict[str, str] = dict()
    instant_next: str = None

    def __str__(self):
        return self.name

    def process_request(self, request: Message):
        """
        process a message: get the data and send response
        :param request: user message to be processed
        """
        ...

    def handle(self, response: Message) -> str:
        """
        get users response
        :param response: users message, by which next state is defined
        :return next state name
        """
        return 'initial'

    @staticmethod
    def _get_next_state_by_name(name: str):
        return get_subclasses().get(name)

    def handler_wrapper(self, response: Message):
        """
        get users response
        :param response: users message, by which next state is defined
        """
        next_state_name = self.universal_states.get(response.text) or self.predefined_states.get(response.text) or self.handle(response)
        next_state = self._get_next_state_by_name(next_state_name)
        assert next_state is not None
        next_state.controller(response)

    def controller(self, message):
        logging.info(f'{self} controller got {message.text}')
        self.process_request(message)
        if self.instant_next:
            self._get_next_state_by_name(self.instant_next).controller(message)
        else:
            self.bot.register_next_step_handler(message, self.handler_wrapper)


def get_subclasses() -> Dict[str, TgStateInterface]:
    return {
        s.name: s() for s in TgStateInterface.__subclasses__()
    }
