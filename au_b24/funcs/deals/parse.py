from typing import Literal, Callable
from ...reqs import post
from ..exceptions import StopParsing

def parse_deals(fn: Callable):
    def wrapper(filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC", **kwargs):
        """
        Parse deals by filters with given function
        
        - ``filters``: filters by fields, allowing '<', '>' and '!' logical symbols, and grouping by []. ID filtering allowing too
        - ``select``: list of selected fields. Passing '*' will select all fields
        - ``order``: sorting by id
        """
        if not isinstance(filters, dict):
            raise ValueError("Filters and select must be a dict")
        if not select:
            raise ValueError("Select is not provided")
        if not isinstance(select, list):
            raise ValueError("Select must be a list")
        if order not in ("ASC", "DESC"):
            raise ValueError("Order must be 'ASC' or 'DESC'")
        if {">ID", "<ID", ">=ID", "<=ID"} & set(filters):
            raise ValueError("ID filtering can't be used with '<', '>', '>=' and '<='")
        filters_copy = {}
        if order == "ASC":
            filters_copy.update({">ID": 0})
            id_key = ">ID"
        else:
            filters_copy.update({"<ID": 2**32})
            id_key = "<ID"
        filters_copy.update(filters)
        while True:
            deals : list[dict] | None = post("crm.deal.list", {"filter": filters_copy, "select": select, "order": {"ID": order}, "start": -1})
            if not deals:
                break
            for deal in deals:
                filters_copy[id_key] = deal["ID"]
                try:
                    fn(deal, **kwargs)
                except StopParsing:
                    return
    return wrapper