from typing import Callable
from ..entities import parse_entities

def parse_companies(fn: Callable):
    return parse_entities("company", fn)
