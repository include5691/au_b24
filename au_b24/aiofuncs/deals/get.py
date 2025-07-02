from typing import Literal
from ...aioreqs import get
from ..entities import get_entities

async def get_deal(deal_id: str | int) -> dict | None:
    """Get deal by given deal_id"""
    deal = await get("crm.deal.get", {"id": deal_id})
    if not deal or not isinstance(deal, dict):
        return None
    return deal

async def get_deals(filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC", limit: int | None = None) -> list[dict] | None:
    """
    Get deals by filters
    """
    return await get_entities(entity_type="deal", filters=filters, select=select, order=order, limit=limit)