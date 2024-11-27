from typing import Literal, Callable
from ...reqs import post
from ..exceptions import StopParsing

def parse_smarts(fn: Callable):
    def wrapper(entity_id: str | int, filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC", **kwargs):
        """
        Parse smarts by filters with given function
        
        - ``entity_id``: entity type id
        - ``filters``: filters by fields, allowing '<', '>' and '!' logical symbols, and grouping by []. ID filtering allowing too
        - ``select``: list of selected fields
        - ``order``: sorting by id
        """
        if not isinstance(filters, dict):
            raise ValueError("Filters and select must be a dict")
        if not isinstance(select, list):
            raise ValueError("Select must be a list")
        if not select:
            raise ValueError("Empty select not allowed smarts")
        if order not in ("ASC", "DESC"):
            raise ValueError("Order must be 'ASC' or 'DESC'")
        if ">ID" in filters and "<ID" in filters:
            raise ValueError("ID filtering not allowing in smarts")
        start = 0
        while True:
            response : list[dict] | None = post("crm.item.list", {"entityTypeId": entity_id, "filter": filters, "select": select, "order": {"ID": order}, "start": start})
            if not response:
                break
            smarts = response.get('items')
            if not smarts:
                break
            for smart in smarts:
                start += 1
                try:
                    fn(smart, **kwargs)
                except StopParsing:
                    return
    return wrapper