from bot.states.interface import StateInterface


class InitialState(StateInterface):
    name = 'initial'
    next_states = {
        '/start': 'initial',
        '/add': 'add',
    }

    def send_message(self, user_id):
        self.bot.send_message(
            user_id,
            'Стартовое сообщение'
        )


