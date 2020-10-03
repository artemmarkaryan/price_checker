from unittest import *
from engine import match
from engine.parsers import asos, farfetch
from engine.errors import UrlNotSupported


class EngineTest(TestCase):
    def test_url_match(self):
        self.assertIsInstance(
            match.match_parser('https://www.farfetch.com/ru/shopping/kids/molo-hali-item-15549420.aspx?storeid=12830'),
            farfetch.FarfatchParser
        )
        self.assertIsInstance(
            match.match_parser('https://www.asos.com/ru/asos-design/chernye-elastichnye-dzhinsy-s-rvanymi-kolenyami-asos-design/prd/10999428'),
            asos.AsosParser
        )
        with self.assertRaises(UrlNotSupported):
            match.match_parser('https://www.nike.com/ru/t/%D0%BA%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0%BA%D0%B8-air-force-1-07-lv8-ng2WcP/DA4660-100'),





