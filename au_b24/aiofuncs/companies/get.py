from typing import Literal
from ...aioreqs import get
from ..entities import get_entities

async def get_company(company_id: str | int) -> dict | None:
    """Get company by given company_id"""
    company = await get("crm.company.get", {"id": company_id})
    if not company or not isinstance(company, dict):
        return None
    return company

async def get_companies(filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC", limit: int | None = None) -> list[dict] | None:
    """
    Get companies by filters
    """
    return await get_entities(entity_type="company", filters=filters, select=select, order=order, limit=limit)
