from ...aioreqs import post


async def create_deal(fields: dict) -> int | None:
    """Create a deal with the provided fields"""
    return await post("crm.deal.add", {"fields": fields})
