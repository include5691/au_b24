from ...aioreqs import post

async def delete_deal(deal_id: str | int) -> bool | None:
    """Delete deal by given lead_id"""
    return await post("crm.deal.delete", {"id": deal_id})