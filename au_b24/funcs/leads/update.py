from ...reqs import post

def update_lead(lead_id: int | str, fields: dict) -> bool | None:
    """Update a lead with given id and fields"""
    return post("crm.lead.update", {"id": lead_id, "fields": fields})