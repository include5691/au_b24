from ...aioreqs import post

async def update_deal(deal_id: int | str, fields: dict) -> bool:
    """Update a deal with given id and fields"""
    return bool(await post("crm.deal.update", {"id": deal_id, "fields": fields}))