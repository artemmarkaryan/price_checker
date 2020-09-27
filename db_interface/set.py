from sqlite3.dbapi2 import Cursor
from db_interface.core import get_cursor


def set_check(
        site_name: str,
        url:       str,
):
    curs: Cursor = get_cursor()
    curs.execute('''
    insert into CHECK 
    ''')