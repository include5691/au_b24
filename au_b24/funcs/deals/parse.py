from typing import Callable
from typing_extensions import deprecated
from ..entities import parse_entities

@deprecated("Use parse_entities instead")
def parse_deals(fn: Callable):
    return parse_entities("deal", fn)