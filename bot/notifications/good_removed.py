from bot.bot import the_bot


def notify(user_id: int, url: str):
    the_bot.send_message(
        user_id,
        f'<b>Товар удалён</b>\n\n' 
        f'Теперь по ссылке {url} ничего нет',
        parse_mode='html'

    )
