from engine.parsers.interface import ParserInterface
from engine.errors import UrlNotSupported
from helpers import filters
import config
import requests
import re
import bs4


class FarfatchParser(ParserInterface):
    site_name = 'farfetch'

    def url_suits(self, url) -> bool:
        return re.match('^https://(farfetch.onelink.me|www.farfetch.com/)(.*)(item-)(\d{8})', url) is not None

    def _get_price(self, url: str) -> float:
        try:
            response = requests.get(url, headers=config.HEADERS).text
            soup = bs4.BeautifulSoup(response, features="lxml")
            price_element = soup.find(lambda tag: tag.attrs.get("data-tstid") == "priceInfo-original")
            price: float = filters.filter_price(price_element.string)
            return price
        except AttributeError:
            raise UrlNotSupported

