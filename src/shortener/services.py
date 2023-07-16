import random
import json

from redis import Redis
from django.conf import settings


def generate_code() -> str:
    symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.sample(symbols, 6))


def validate_url(base_url: str) -> str:
    if base_url.startswith('https://') or base_url.startswith('http://'):
        return base_url
    else:
        return 'https://' + base_url


class LinkSerivce:
    def __init__(self) -> None:
        self.redis = Redis(host=settings.REDIS_HOST, port=6379, db=0)

    def get_short_url(self, code):
        if settings.SUPPORT_SECURE:
            return 'https://' + settings.DOMAIN + '/' + code
        else:
            return 'http://' + settings.DOMAIN + '/' + code

    def create_link(self, url):
        code = generate_code()
        self.redis.set(
            code,
            json.dumps({'url': validate_url(url), 'usage_count': 0}),
            ex=60 * 60 * 6,
        )  # 6 hours
        return code

    def register_usage(self, code):
        value = json.loads(self.redis.get(code))
        value['usage_count'] += 1
        self.redis.set(code, json.dumps(value), keepttl=True)

    def get_usage_count(self, code):
        value = json.loads(self.redis.get(code))
        return value['usage_count']

    def get_url(self, code):
        value = json.loads(self.redis.get(code))
        return value['url']

    def close(self):
        self.redis.close()
