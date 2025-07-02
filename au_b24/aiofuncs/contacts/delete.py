from ...aioreqs import post

async def delete_contact(contact_id: str | int) -> bool | None:
    """Delete contact by given lead_id"""
    return await post("crm.contact.delete", {"id": contact_id})