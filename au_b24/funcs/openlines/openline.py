from typing import Literal
from ...reqs import post

def get_openlines(entity_id: int | str, entity_type: Literal["lead", "deal", "contact"]) -> list[dict] | None:
    """Get current openlines by given entity_id and entity_type"""
    result = post("imopenlines.crm.chat.get", {"CRM_ENTITY": entity_id, "CRM_ENTITY_TYPE": entity_type})
    if result and isinstance(result, list):
        return [ol for ol in result if isinstance(ol, dict)]
    return None

def get_last_openline_id(entity_id: int | str, entity_type: Literal["lead", "deal", "contact"]) -> int | None:
    """Get last openline id by given entity_id and entity_type"""
    ol_id = post("imopenlines.crm.chat.getLastId", {"CRM_ENTITY": entity_id, "CRM_ENTITY_TYPE": entity_type})
    if ol_id and isinstance(ol_id, int):
        return ol_id
    return None