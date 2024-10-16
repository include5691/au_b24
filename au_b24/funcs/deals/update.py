from ...reqs import post

def update_deal(deal_id: int | str, fields: dict) -> bool | None:
    """Update a deal with given id and fields"""
    return post("crm.deal.update", {"id": deal_id, "fields": fields})