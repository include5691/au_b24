from typing import Callable
from ..entities import parse_entities

def parse_contacts(fn: Callable):
    return parse_entities("contact", fn)