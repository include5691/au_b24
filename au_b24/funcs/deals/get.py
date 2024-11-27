from typing import Literal
from ...reqs import post, get

def get_deal(deal_id: str | int) -> dict | None:
    """Get deal by given deal_id"""
    return get("crm.deal.get", {"id": deal_id})

def get_deals(filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC", limit: int | None = None) -> list[dict]:
    """
    Get deals by filters

    :param filters: filters by fields, allowing '<', '>' and '!' logical symbols, and grouping by []. ID filtering allowing too
    :param select: list of selected fields
    :param order: sorting by id
    """
    if not isinstance(filters, dict):
        raise ValueError("Filters and select must be a dict")
    if not isinstance(select, list):
        raise ValueError("Select must be a list")
    if order not in ("ASC", "DESC"):
        raise ValueError("Order must be 'ASC' or 'DESC'")
    if ">ID" in filters and "<ID" in filters:
        raise ValueError("ID filtering can't be used with '<' and '>'")
    if limit and limit <= 0:
        raise ValueError("Limit must be greater than 0")
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
    result = []
    while True:
        deals : list[dict] | None = post("crm.deal.list", {"filter": f, "select": select, "order": {"ID": order}, "start": -1})
        if not deals:
            break
        for deal in deals:
            if limit and len(result) >= limit:
                return result
            f[id_key] = deal["ID"]
            result.append(deal)
    return result if result else None