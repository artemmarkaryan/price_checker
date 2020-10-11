import logging


logging.basicConfig()


class ParserInterface:
    site_name: str = ''

    def url_suits(self, url) -> bool:
        ...

    def get_price(self, url: str) -> float:
        ...

    def __str__(self):
        return self.site_name