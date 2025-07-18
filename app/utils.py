def format_price(price: float) -> str:
    rounded_price = round(price, 2)
    return (
        str(int(rounded_price))
        if rounded_price.is_integer()
        else str(rounded_price)
    )
