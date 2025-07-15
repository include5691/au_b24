from ...aioreqs import post

async def update_contact(contact_id: str | int, fields: dict) -> bool:
    "Update a contact with given id and fields"
    return bool(await post("crm.contact.update", {"id": contact_id, "fields": fields}))
