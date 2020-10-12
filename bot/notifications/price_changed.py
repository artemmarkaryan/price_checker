from bot.bot import notification_bot


def notify(
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
