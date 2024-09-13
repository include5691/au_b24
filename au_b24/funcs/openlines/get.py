from typing import Literal
from ...requests_ import post

def get_openlines(entity_id: int | str, entity_type: Literal["lead", "deal", "contact"]) -> list[dict] | None:
    """Get current openlines by given entity_id and entity_type"""
    result = post("imopenlines.crm.chat.get", {"CRM_ENTITY": entity_id, "CRM_ENTITY_TYPE": entity_type})
    if result and isinstance(result, list):
        return result
    return None

def get_last_openline_id(entity_id: int | str, entity_type: Literal["lead", "deal", "contact"]) -> int | None:
    """Get last openline id by given entity_id and entity_type"""
    return post("imopenlines.crm.chat.getLastId", {"CRM_ENTITY": entity_id, "CRM_ENTITY_TYPE": entity_type})