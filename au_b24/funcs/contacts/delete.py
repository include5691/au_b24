from ...reqs import post, get

def delete_contact(contact_id: str | int) -> bool | None:
    """Delete contact by given lead_id"""
    return post("crm.contact.delete", {"id": contact_id})