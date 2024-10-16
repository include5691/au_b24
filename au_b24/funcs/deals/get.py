from ...reqs import post, get

def get_deal(deal_id) -> dict | None:
    """Get deal by given deal_id"""
    return get("crm.deal.get", {"id": deal_id})