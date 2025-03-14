from ...reqs import post

def update_lead(lead_id: int | str, fields: dict) -> bool:
    """Update a lead with given id and fields"""
    return bool(post("crm.lead.update", {"id": lead_id, "fields": fields}))