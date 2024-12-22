from typing import Callable
from typing_extensions import deprecated
from ..entities import parse_entities

@deprecated("Use parse_entities instead")
def parse_leads(fn: Callable):
    return parse_entities("lead", fn)