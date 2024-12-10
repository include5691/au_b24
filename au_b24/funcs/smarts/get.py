from typing import Literal
from ...reqs import post, get

def get_smart(entity_id: str | int, smart_id: str | int) -> dict | None:
    """Get smart by given entity type id and smart item id"""
    response = get("crm.item.get", {"entityTypeId": entity_id, "id": smart_id})
    if not response or not isinstance(response, dict):
        return None
    item = response.get("item")
    if not item or not isinstance(item, dict):
        return None
    return item

def get_smarts(entity_id: str | int, filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC", limit: int | None = None) -> list[dict]:
    """
    Get smarts by filters  
    ID filtering allowed

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
        raise ValueError("Empty select not allowed in smarts")
    if order not in ("ASC", "DESC"):
        raise ValueError("Order must be 'ASC' or 'DESC'")
    if limit and limit <= 0:
        raise ValueError("Limit must be greater than 0")
    if "id" not in select and "ID" not in select:
        select.append("id")
    result = []
    last_smart_id = None
    while True:
        response : list[dict] | None = post("crm.item.list", {"entityTypeId": entity_id, "filter": filters, "select": select, "order": {"ID": order}, "start": len(result)})
        if not response:
            break
        smarts = response.get('items')
        if not smarts:
            break
        for smart in smarts:
            if not smart or not isinstance(smart, dict):
                continue
            smart_id = smart.get("id")
            if not last_smart_id:
                last_smart_id = smart_id
            if order == "ASC" and smart_id < last_smart_id:
                return result
            elif order == "DESC" and smart_id > last_smart_id:
                return result
            last_smart_id = smart_id
            result.append(smart)
            if limit and len(result) >= limit:
                return result
    return result if result else None