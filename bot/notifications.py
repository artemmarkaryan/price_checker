from bot.bot import notification_bot


def item_removed(user_id: int, url: str):
    notification_bot.send_message(
        user_id,
        f'<b>Товар удалён</b>\n\n'
        f'Теперь по ссылке {url} ничего нет',
    )


def price_changed(
        user_id: int,
        old_price: float,
        new_price: float,
        url
):
    notification_bot.send_message(
        user_id,
        f"<b>Цена изменилась</b>\n"
        f"Было {old_price}₽, теперь {new_price}₽\n\n"
        f"<a href='{url}'>Ссылка на товар</a>",
    )
