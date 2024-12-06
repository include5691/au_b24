from typing import Literal, Callable
from ...reqs import post
from ..exceptions import StopParsing

def parse_leads(fn: Callable):
    def wrapper(filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC", **kwargs):
        """
        Parse leads by filters with given function
        
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
        else:
            filters_copy.update({"<ID": 2**32})
        if "<ID" in filters:
            id_key = "<ID"
        else:
            id_key = ">ID"
        filters_copy.update(filters)
        while True:
            leads : list[dict] | None = post("crm.lead.list", {"filter": filters_copy, "select": select, "order": {"ID": order}, "start": -1})
            if not leads:
                break
            for lead in leads:
                filters_copy[id_key] = lead["ID"]
                try:
                    fn(lead, **kwargs)
                except StopParsing:
                    return
    return wrapper