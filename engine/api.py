import database
import engine
from helpers import filters
import logging


def add_link(platform: str, user_id: int, text: str) -> bool:
    try:
        url: str = filters.get_links_from_text(text)
        logging.info(f'got url {url} from {text}')
        if url is None:
            return False

        parser = engine.match.match_parser_by_url(url)
        database.facade.check.add_check(
            platform_name=platform,
            user_id=user_id,
            url=url,
            parser=parser,
        )
        return True

    except engine.errors.UrlNotSupported:
        return False
