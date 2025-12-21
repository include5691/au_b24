from ...aioreqs import post


async def create_contact(fields: dict) -> int | None:
    """
    Create a contact with given fields
    Accepts phone in "PHONE": [{"VALUE": "+7234567890", "VALUE_TYPE": "WORK"}] format
    """
    return await post("crm.contact.add", {"fields": fields})
