def filter_price(price: str) -> str:
    new_price = ""
    for ch in price:
        if ch == ',' or ch == '.':
            break
        if ch.isdigit():
            new_price += ch
    return new_price
