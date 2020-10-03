from engine.parsers.interface import ParserInterface
from engine.errors import UrlNotSupported
import logging


def match_parser(url: str) -> ParserInterface:

    for parser in ParserInterface.__subclasses__():
        parser = parser()
        if parser.url_suits(url):
            logging.info(f'{url} matches {parser}')
            return parser

    logging.info(f'{url} didnt match any parser')
    raise UrlNotSupported

