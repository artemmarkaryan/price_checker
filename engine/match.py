from engine.parsers.interface import ParserInterface
from engine.errors import UrlNotSupported
import logging


def match_parser_by_url(url: str) -> ParserInterface:

    for parser in ParserInterface.__subclasses__():
        parser = parser()
        if parser.url_suits(url):
            logging.info(f'{url} matches {parser}')
            return parser

    logging.info(f'{url} didnt match any parser')
    raise UrlNotSupported


def match_parser_by_name(name: str) -> ParserInterface:
    for parser in ParserInterface.__subclasses__():
        if name == parser.site_name:
            return parser()
