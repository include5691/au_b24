from ...reqs import post

def create_lead(fields: dict) -> int | None:
    """
    Create a new lead with the given fields.
    """
    return post("crm.lead.add", fields)