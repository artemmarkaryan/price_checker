from parser.parser import ParserInterface
from urllib.parse import urlparse
import requests
import re


class AsosParser(ParserInterface):
    site_name = 'asos'

    def url_suits(self, url) -> bool:
        return re.match('(asos).+prd/(\d+)', url) is not None

    def get_price(self, url: str) -> float:
        product_id = re.match('.*prd/(\d+)', url)[1]
        response = requests.get(
            f'https://www.asos.com/api/product/catalogue/v3/stockprice?productIds={product_id}&store=RU&currency=RUB&keyStoreDataversion=3pmn72e-27'
        ).json()
        price = response[0]['productPrice']['current']['value']
        return price
