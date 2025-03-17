import os
from typing import Literal

def create_crm_link(entity_type: Literal['lead', 'deal', 'contact'], entity_id: int | str) -> str:
    """Create a link to a lead with given id"""
    return f"https://{os.getenv('BITRIX_ID')}.bitrix24.ru/crm/{entity_type}/details/{entity_id}/"