from db_interface.models import *


def add_site(site_name: str):
    return Site.create(site_name=site_name)