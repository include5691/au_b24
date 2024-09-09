from typing import Literal, Callable
from ..._requests import post, get

def parse_leads(fn: Callable):
    def wrapper(filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC"):
        """
        Parse leads by filters with given function
        
        - ``filters``: filters by fields, allowing '<', '>' and '!' logical symbols, and grouping by []. ID filtering allowing too
        - ``select``: list of selected fields
        - ``order``: sorting by id
        """
        if not isinstance(filters, dict) or not isinstance(select, list):
            raise ValueError("Filters and select must be a dict and a list")
        if order not in ("ASC", "DESC"):
            raise ValueError("Order must be 'ASC' or 'DESC'")
        if ">ID" in filters and "<ID" in filters:
            raise ValueError("ID filtering can't be used with '<' and '>'")
        f = {}
        if ">ID" in filters:
            order = "ASC"
        elif "<ID" in filters:
            order = "DESC"
        elif order == "ASC":
            f.update({">ID": 0})
        else:
            f.update({"<ID": 2**32})
        if "<ID" in filters:
            id_key = "<ID"
        else:
            id_key = ">ID"
        f.update(filters)
        while True:
            leads : list[dict] | None = post("crm.lead.list", {"filter": f, "select": select, "order": {"ID": order}, "start": -1})
            if not leads:
                break
            for lead in leads:
                f[id_key] = lead["ID"]
                fn(lead)
    return wrapper