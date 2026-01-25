from typing import Literal
from ...reqs import get
from ..entities import get_entities

def get_company(company_id: str | int) -> dict | None:
    """Get company by given company_id"""
    company = get("crm.company.get", {"id": company_id})
    if not company or not isinstance(company, dict):
        return None
    return company

def get_companies(filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC", limit: int | None = None) -> list[dict] | None:
    """
    Get companies by filters
    """
    return get_entities(entity_type="company", filters=filters, select=select, order=order, limit=limit)
