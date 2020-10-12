from bot.states.interface import StateInterface


class AddState(StateInterface):
    name = 'add'

    def send_message(self, user_id):
        self.bot.send_message(
            user_id,
            'add message'
        )


# def handle_add(m: Message):
#     the_bot.send_message(
#         m.chat.id,
#         'Пришлите ссылку на товар',
#         reply_markup=generate_cancel()
#     )
#     the_bot.register_next_step_handler(m, handle_url)
#
#
# def handle_url(m: Message):
#     if m.text == KB_BUTTONS['CANCEL']:
#         views.start.send_initial_message(m.chat.id)
#         return
#
#     if len(m.text.split()) > 1:
#         the_bot.send_message(m.chat.id, 'Пришлите только ссылку')
#         the_bot.register_next_step_handler(m, handle_url)
#         return
#
#     url = m.text
#     try:
#         parser = match_parser_by_url(url)
#         check, created = facade.check.add_check(m.chat.id, parser, url)
#         if created:
#             the_bot.send_message(
#                 m.chat.id,
#                 f'Цена: {check.price_verbose}\nТеперь ссылка отслеживается'
#             )
#         else:
#             the_bot.send_message(
#                 m.chat.id,
#                 f'Цена: {check.price_verbose}\nЭта ссылка уже отслеживается'
#             )
#     except UrlNotSupported:
#         handle_add(m)
