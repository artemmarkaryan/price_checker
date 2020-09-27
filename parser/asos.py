import requests
from parser.parser import Parser


class AsosParser(Parser):
    def __init__(self):
        super().__init__()
        self.site_name = "asos"

    def fetch(self):
        pass

    def set(self):
        pass
