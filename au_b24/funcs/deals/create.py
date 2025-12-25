from ...reqs import post


def create_deal(fields: dict) -> int | None:
    """Create a deal with the provided fields"""
    return post("crm.deal.add", {"fields": fields})
