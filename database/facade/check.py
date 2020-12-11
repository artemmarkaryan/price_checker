from database.models import *
from database import errors
from engine.parsers.interface import ParserInterface
import peewee
import logging


def add_check(
        platform_name: str,
        user_id: int,
        parser: ParserInterface,
        url: str
) -> (Check, bool):
    users: User = User.select().join(Platform).where(
        User.user_id == user_id,
        Platform.name == platform_name
    )
    if len(users) != 1:
        raise errors.DoesNotExist
    else:
        user = users[0]

    site: Site = Site.get(Site.name == parser.site_name)
    check, created = Check.get_or_create(
        user=user,
        site=site,
        url=url,
        price=parser.get_price(url)
    )
    return check, created


def get_checks() -> peewee.Query:
    return Check.select().join(Site)


def update_check(check_id: int, new_price: float):
    q = Check.update({Check.price: new_price}).where(Check.id == check_id)
    q.execute()

