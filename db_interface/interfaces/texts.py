from db_interface.models import Texts
from db_interface.errors import *


def get(name, text_id=None) -> str:
    if text_id:
        instances = Texts.select(Texts.id == text_id)
    else:
        instances = Texts.select(Texts.name == name)

    if len(instances) == 0:
        raise DoesNotExist
    elif len(instances) == 1:
        return instances[0]
    else:
        raise TooManyValues
