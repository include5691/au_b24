from typing import Literal
from ...reqs import post, get

def get_contact(contact_id: str | int) -> dict | None:
    """Get contact by given contact_id"""
    return get("crm.contact.get", {"id": contact_id})

def get_contacts(filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC", limit: int | None = None) -> list[dict]:
    """
    Get contacts by filters

    :param filters: filters by fields, allowing '<', '>' and '!' logical symbols, and grouping by []. ID filtering allowing too
    :param select: list of selected fields. Passing '*' will select all fields
    :param order: sorting by id
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
    if limit and limit <= 0:
        raise ValueError("Limit must be greater than 0")
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
    result = []
    while True:
        contacts : list[dict] | None = post("crm.contact.list", {"filter": filters_copy, "select": select, "order": {"ID": order}, "start": -1})
        if not contacts:
            break
        for contact in contacts:
            if limit and len(result) >= limit:
                return result
            filters_copy[id_key] = contact["ID"]
            result.append(contact)
    return result if result else None