from db_interface.models import *


def add_check(user_id: int, parser: ParserInterface, url: str) -> Check:
    user: User = User.get(User.id == user_id)
    site: Site = Site.get(Site.name == parser.site_name)
    check = Check.create(
        user=user,
        site=site,
        url=url,
        price=parser.get_price(url)
    )
    return check

