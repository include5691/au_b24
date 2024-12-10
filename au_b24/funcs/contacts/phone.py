from ...reqs import get

def get_phone_by_contact(contact_id: str | int) -> str | None:
    """Get phone by given contact_id"""
    contact = get("crm.contact.get", {"id": contact_id})
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