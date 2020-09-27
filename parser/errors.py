
class ElementNotFound(Exception):
    def __init__(self, selector: str):
        self.message = f"{selector} not found"
