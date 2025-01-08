from typing import Literal
from ...reqs import get
from ..entities import get_entities

def get_contact(contact_id: str | int) -> dict | None:
    """Get contact by given contact_id"""
    contact = get("crm.contact.get", {"id": contact_id})
    if not contact or not isinstance(contact, dict):
        return None
    return contact

def get_contacts(filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC", limit: int | None = None) -> list[dict] | None:
    """
    Get contacts by filters
    """
    return get_entities(entity_type="contact", filters=filters, select=select, order=order, limit=limit)