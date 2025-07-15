from ...aioreqs import post

async def update_lead(lead_id: int | str, fields: dict) -> bool:
    """Update a lead with given id and fields"""
    return bool(await post("crm.lead.update", {"id": lead_id, "fields": fields}))