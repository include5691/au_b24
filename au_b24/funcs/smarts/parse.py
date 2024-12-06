from typing import Literal, Callable
from ...reqs import post
from ..exceptions import StopParsing

def parse_smarts(fn: Callable):
    def wrapper(entity_id: str | int, filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC", **kwargs):
        """
        Parse smarts by filters with given function
        ID filtering allowed

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
        if "id" not in select and "ID" not in select:
            select.append("id")
        start = 0
        last_smart_id = None
        while True:
            response: list[dict] | None = post("crm.item.list", {"entityTypeId": entity_id, "filter": filters, "select": select, "order": {"ID": order}, "start": start})
            if not response:
                break
            smarts = response.get('items')
            if not smarts:
                break
            for smart in smarts:
                start += 1
                smart_id = smart.get("id")
                if not last_smart_id:
                    last_smart_id = smart_id
                if order == "ASC" and smart_id < last_smart_id:
                    return
                elif order == "DESC" and smart_id > last_smart_id:
                    return
                last_smart_id = smart_id
                try:
                    fn(smart, **kwargs)
                except StopParsing:
                    return
    return wrapper