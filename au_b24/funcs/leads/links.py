import os

def create_lead_link(lead_id: int | str) -> str:
    """Create a link to a lead with given id"""
    return f"https://{os.getenv('BITRIX_ID')}.bitrix24.ru/crm/lead/details/{lead_id}/"