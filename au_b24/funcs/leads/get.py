from typing import Literal
from ...reqs import post, get

def get_lead(lead_id: str | int) -> dict | None:
    """Get lead by given lead_id"""
    return get("crm.lead.get", {"id": lead_id})

def get_leads(filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC", limit: int | None = None) -> list[dict]:
    """
    Get leads by filters

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
        leads : list[dict] | None = post("crm.lead.list", {"filter": f, "select": select, "order": {"ID": order}, "start": -1})
        if not leads:
            break
        for lead in leads:
            if limit and len(result) >= limit:
                return result
            f[id_key] = lead["ID"]
            result.append(lead)
    return result if result else None