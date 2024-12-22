from typing import Literal
from ..reqs import post

def get_calls(filters: dict, order: Literal["ASC", "DESC"] = "ASC", limit: int | None = None) -> list[dict]:
    """
    Get calls by filters
    """
    if not isinstance(filters, dict):
        raise ValueError("Filters must be a dict")
    if order not in ("ASC", "DESC"):
        raise ValueError("Order must be 'ASC' or 'DESC'")
    if limit and limit <= 0:
        raise ValueError("Limit must be greater than 0")
    filters_copy = filters.copy()
    if order == "ASC":
        filters_copy.update({">ID": 0})
        id_key = ">ID"
    else:
        filters_copy.update({"<ID": 2**32})
        id_key = "<ID"
    result = []
    while True:
        calls: list[dict] | None = post("voximplant.statistic.get", {"filter": filters_copy, "sort": "ID", "order": order, "start": -1})
        if not calls:
            break
        for call in calls:
            if not call or not isinstance(call, dict):
                continue
            filters_copy[id_key] = call["ID"]
            result.append(call)
            if limit and len(result) >= limit:
                return result
    return result if result else None