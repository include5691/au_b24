from typing import Literal
from ...reqs import post, get

def get_smart(entity_id: str | int, smart_id: str | int) -> dict | None:
    """Get smart by given entity type id and smart item id"""
    response = get("crm.item.get", {"entityTypeId": entity_id, "id": smart_id})
    if not response:
        return None
    return response.get("item")

def get_smarts(entity_id: str | int, filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC", limit: int | None = None) -> list[dict]:
    """
    Get smarts by filters

    :param entity_id: entity type id
    :param filters: filters by fields, allowing '<', '>' and '!' logical symbols, and grouping by []. ID filtering allowing too
    :param select: list of selected fields
    :param order: sorting by id
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
        raise ValueError("ID filtering can't be used with '<' and '>'")
    if limit and limit <= 0:
        raise ValueError("Limit must be greater than 0")
    result = []
    while True:
        response : list[dict] | None = post("crm.item.list", {"entityTypeId": entity_id, "filter": filters, "select": select, "order": {"ID": order}, "start": len(result)})
        if not response:
            break
        smarts = response.get('items')
        if not smarts:
            break
        for smart in smarts:
            if limit and len(result) >= limit:
                return result
            result.append(smart)
    return result if result else None