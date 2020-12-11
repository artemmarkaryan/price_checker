from engine.parsers.interface import ParserInterface
from engine.errors import UrlNotSupported
import requests
import re
import pprint
pp = pprint.PrettyPrinter().pprint


class AsosParser(ParserInterface):
    site_name = 'asos'

    def url_suits(self, url) -> bool:
        return re.match('https://www.asos.com/.*/prd/(\d{8}).*', url) is not None

    def _get_price(self, url: str) -> float:
        product_id = re.match('.*prd/(\d+)', url)[1]
        response = requests.get(
            f'https://www.asos.com/api/product/catalogue/v3/stockprice?productIds={product_id}&store=RU&currency=RUB&keyStoreDataversion=3pmn72e-27'
        )
        try:
            data = response.json()
            price = data['price']['current']['value']
            return price
        except ValueError and KeyError:
            raise UrlNotSupported


if __name__ == '__main__':
    print(
        AsosParser()._get_price(
            'https://www.asos.com/ru/prd/12759000'
        )
    )