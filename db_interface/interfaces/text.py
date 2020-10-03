from db_interface.models import Text
from db_interface.errors import *
import logging


def get(name, text_id=None) -> str:
    if text_id:
        instances = Text.select().where(Text.id == text_id)
    else:
        instances = Text.select().where(Text.name == name)

    if len(instances) == 0:
        raise DoesNotExist
    elif len(instances) == 1:
        text: Text = instances[0]
        logging.info(f'selected {text}')
        return text.text
    else:
        raise TooManyValues
