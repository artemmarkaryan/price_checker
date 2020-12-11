import unittest
from engine.parsers import asos, farfetch
import logging


class ParserTests(unittest.TestCase):

    def test_parsers(self):
        # update prices before test
        cases = {
            asos.AsosParser(): {
                'https://www.asos.com/ru/topman/topman-jersey-blazer-in-grey/prd/22260090?colourwayid=60385393&SearchQuery=&cid=5678': 2190,
            },

            # farfetch.FarfatchParser(): {
            #     "https://www.farfetch.com/ru/shopping/men/balmain--item-15483029.aspx?storeid=9359": 158700,
            #     "https://www.farfetch.com/ru/shopping/men/loewe--item-15119244.aspx": 31262,
            # }

        }

        for parser, tests in cases.items():
            for url, price in tests.items():
                got_price = parser.get_price(url)
                print(got_price)
                self.assertTrue(got_price == price)


if __name__ == '__main__':
    unittest.main()
