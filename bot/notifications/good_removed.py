from bot.bot import notification_bot


def notify(user_id: int, url: str):
    notification_bot.send_message(
        user_id,
        f'<b>Товар удалён</b>\n\n' 
        f'Теперь по ссылке {url} ничего нет',
    )
