from database.models import *
import peewee


def add_check(user_id: int, parser, url: str) -> (Check, bool):
    user: User = User.get(User.id == user_id)
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

