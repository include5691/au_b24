from typing import Callable
from ..entities import parse_entities

def parse_deals(fn: Callable):
    return parse_entities("deal", fn)