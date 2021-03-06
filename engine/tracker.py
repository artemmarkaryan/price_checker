from database.facade import check
from engine.parsers.interface import ParserInterface
from engine.errors import UrlNotSupported
from engine.match import match_parser_by_name
from typing import Dict
from telegram import notifications
import logging

parsers: Dict[str, ParserInterface] = {p.site_name: p() for p in ParserInterface.__subclasses__()}


def execute():
    logging.info('execute tracking')
    for instance in check.get_checks():
        try:
            new_price = parsers[instance.site.name].get_price(instance.url)
            check.update_check(instance.id, new_price)
            if new_price != instance.price:
                logging.info('notifying')
                notifications.price_changed(
                    user_id=instance.user,
                    old_price=instance.price,
                    new_price=new_price,
                    url=instance.url
                )

        except UrlNotSupported:
            notifications.good_removed(
                user_id=instance.user,
                url=instance.url
            )
