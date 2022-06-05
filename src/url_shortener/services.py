import random


def _generate_code() -> str:
    symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.sample(symbols, 6))


def _validate_url(base_url: str) -> str:
    if (
        base_url.startswith('https://') 
        or 
        base_url.startswith('http://')
    ):
        return base_url
    else:
        return 'https://' + base_url
