import unittest
from engine.parsers import asos, farfetch
import logging


class ParserTests(unittest.TestCase):

    def test_parsers(self):
        # update prices before test
        cases = {
            asos.AsosParser(): {
                "https://www.asos.com/ru/puma/belye-vysokie-krossovki-puma-cali-sport/prd/20928503?clr=puma-white-puma-whit&colourwayid=60100435&SearchQuery=&cid=1931": 7645.0,

                "https://www.asos.com/ru/na-kd/oranzhevoe-plate-mini-s-tsvetochnym-printom-i-kvadratnym-vyrezom-na-kd/prd/20172273?clr=oranzhevyj&colourwayid=60014515&SearchQuery=&cid=7046": 1790.0,

                "https://www.asos.com/ru/na-kd/oranzhevoe-plate-mini-s-tsvetochnym-printom-i-kvadratnym-vyrezom-na-kd/prd/00000000?clr=oranzhevyj&colourwayid=60014515&SearchQuery=&cid=7046": 1790.0,
            },

            farfetch.FarfatchParser(): {
                "https://www.farfetch.com/ru/shopping/men/balmain--item-15483029.aspx?storeid=9359": 158700,
            }

        }

        for parser, tests in cases.items():
            for url, price in tests.items():
                self.assertTrue(parser.get_price(url) == price)


if __name__ == '__main__':
    unittest.main()
