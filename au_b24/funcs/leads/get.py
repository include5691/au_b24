from typing import Literal
from ..._requests import post, get

def get_lead(lead_id) -> dict | None:
    """Get lead by given lead_id"""
    return get("crm.lead.get", {"id": lead_id})

def get_leads(filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC"):
    """
    Get leads by filters
    
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