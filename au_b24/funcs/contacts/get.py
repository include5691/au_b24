from typing import Literal
from ...reqs import post, get

def get_contact(contact_id: str | int) -> dict | None:
    """Get contact by given contact_id"""
    return get("crm.contact.get", {"id": contact_id})

def get_contacts(filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC", limit: int | None = None) -> list[dict]:
    """
    Get contacts by filters

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
    contacts_ = []
    while True:
        contacts : list[dict] | None = post("crm.contact.list", {"filter": f, "select": select, "order": {"ID": order}, "start": -1})
        if not contacts:
            break
        for contact in contacts:
            if limit and len(contacts_) >= limit:
                return contacts_
            f[id_key] = contact["ID"]
            contacts_.append(contact)
    return contacts_