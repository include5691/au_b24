from ....aioreqs import post

async def get_deal_product_rows(deal_id: int | str) -> list[dict] | None:
    """Get product rows for a deal (crm.deal.productrows.get)"""
    result = await post("crm.deal.productrows.get", {"id": deal_id})
    if not result or not isinstance(result, list):
        return None
    return result

async def set_deal_product_rows(deal_id: int | str, rows: list[dict]) -> bool:
    """Set product rows for a deal (crm.deal.productrows.set)"""
    return bool(await post("crm.deal.productrows.set", {"id": deal_id, "rows": rows}))
