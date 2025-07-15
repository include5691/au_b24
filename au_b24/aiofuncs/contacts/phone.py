from .get import get_contact

async def get_phone_by_contact(contact_id: str | int | None = None, contact: dict | None = None) -> str | None:
    """Get phone by given contact_id or by contact itself"""
    contact = contact or await get_contact(contact_id)
    if not contact or not isinstance(contact, dict):
        return None
    phone_data_list = contact.get("PHONE")
    if not phone_data_list or not isinstance(phone_data_list, list):
        return None
    phone_data = phone_data_list[0]
    if not phone_data or not isinstance(phone_data, dict):
        return None
    phone = phone_data.get("VALUE")
    if not phone or not isinstance(phone, str):
        return None
    return phone