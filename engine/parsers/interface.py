from db_interface.models import *
import logging

logging.basicConfig()


class ParserInterface:
    site_name: str = ''
    if site_name != '':
        site_instance: Site = Site.get(Site.name == site_name)

    def url_suits(self, url) -> bool:
        ...

    def get_price(self, url: str) -> float:
        ...

    def create_check(self, user: User, url: str):
        Check.create(
            site=self.site_instance,
            user=user,
            url=url,
            value=self.get_price(url)
        )
