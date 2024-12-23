from typing import Callable
from ..entities import parse_entities

def parse_leads(fn: Callable):
    return parse_entities("lead", fn)