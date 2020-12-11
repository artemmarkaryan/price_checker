from telegram.states.interface import TgStateInterface
from helpers import kb_generator


class HelpState(TgStateInterface):
    name = 'help'

    def process_request(self, request):
        self.bot.send_message(
            request.chat.id,
            '/start - вернуться на главную\n'
            '/help - список команд\n'
            '/add - добавить продукт для отслеживания\n'
            '/products - просмотреть свои продукты',
            reply_markup=kb_generator.generate_reply(
                '/start', '/help', '/add', '/products'
            )
        )
