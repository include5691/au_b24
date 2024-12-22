from typing import Literal
from ...reqs import get
from ..entities import get_entities

def get_lead(lead_id: str | int) -> dict | None:
    """Get lead by given lead_id"""
    lead = get("crm.lead.get", {"id": lead_id})
    if not lead or not isinstance(lead, dict):
        return None
    return lead

def get_leads(filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC", limit: int | None = None) -> list[dict]:
    """
    Get leads by filters
    """
    return get_entities(entity_type="lead", filters=filters, select=select, order=order, limit=limit)