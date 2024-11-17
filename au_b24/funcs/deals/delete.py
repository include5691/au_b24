from ...reqs import post, get

def delete_deal(deal_id: str | int) -> bool | None:
    """Delete deal by given lead_id"""
    return post("crm.deal.delete", {"id": deal_id})