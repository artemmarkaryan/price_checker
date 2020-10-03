class DoesNotExist(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TooManyValues(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
