import logging
import time


class ParserInterface:
    site_name: str = ''

    def url_suits(self, url) -> bool:
        ...

    def _get_price(self, url: str) -> float:
        ...

    def get_price(self, url: str) -> float:
        old_time = time.time()
        price = self._get_price(url)
        logging.info(f'got price in {str(time.time() - old_time)}; url: {url}')
        return price

    def __str__(self):
        return self.site_name
