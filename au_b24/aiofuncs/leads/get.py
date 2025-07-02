from typing import Literal

from ...aioreqs import get
from ..entities import get_entities

async def get_lead(lead_id: str | int) -> dict | None:
    """Get lead by given lead_id"""
    lead = await get("crm.lead.get", {"id": lead_id})
    if not lead or not isinstance(lead, dict):
        return None
    return lead

async def get_leads(filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC", limit: int | None = None) -> list[dict] | None:
    """
    Get leads by filters
    """
    return await get_entities(entity_type="lead", filters=filters, select=select, order=order, limit=limit)