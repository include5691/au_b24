from ...aioreqs import post

async def create_lead(fields: dict) -> int | None:
    """
    Create a new lead with the given fields.
    """
    return await post("crm.lead.add", fields)