def _make_digital(string) -> str:
    return ''.join([c for c in string if c.isdigit()])


def filter_price(price: str, delimiter: str = None) -> float:

    if delimiter is None:
        new_price = float(_make_digital(price))

    else:
        roubles, kopeck = price.split(delimiter)
        roubles = _make_digital(roubles)
        kopeck = _make_digital(kopeck)
        new_price = float(roubles) + float(kopeck)/100

    return new_price
