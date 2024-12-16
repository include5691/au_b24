from .get import get_lead

def get_phone_by_lead(lead_id: str | int | None = None, lead: dict | None = None) -> str | None:
    """Get phone by given lead_id or by lead itself"""
    lead = lead or get_lead(lead_id)
    if not lead or not isinstance(lead, dict):
        return None
    phone_data_list = lead.get("PHONE")
    if not phone_data_list or not isinstance(phone_data_list, list):
        return None
    phone_data = phone_data_list[0]
    if not phone_data or not isinstance(phone_data, dict):
        return None
    phone = phone_data.get("VALUE")
    if not phone or not isinstance(phone, str):
        return None
    return phone