from typing import Literal
from ...aioreqs import get
from ..entities import get_entities

async def get_product(product_id: str | int) -> dict | None:
    """Get product by given product_id"""
    product = await get("crm.product.get", {"id": product_id})
    if not product or not isinstance(product, dict):
        return None
    return product

async def get_products(filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC", limit: int | None = None):
    """
    Get products by filters
    """
    return await get_entities(entity_type="product", filters=filters, select=select, order=order, limit=limit)