from ...aioreqs import post

async def delete_lead(lead_id: str | int) -> bool | None:
    """Delete lead by given lead_id"""
    return await post("crm.lead.delete", {"id": lead_id})