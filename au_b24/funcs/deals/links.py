import os

def create_deal_link(deal_id: int | str) -> str:
    """Create a deal to a lead with given id"""
    return f"https://{os.getenv('BITRIX_ID')}.bitrix24.ru/crm/deal/details/{deal_id}/"