from typing import Literal
from ..._requests import post

def get_openline_id(entity_id: int | str, entity_type: Literal["lead", "deal", "contact"]) -> int | None:
    """Get last openline id by given entity_id and entity_type"""
    return post("imopenlines.crm.chat.getLastId", {"CRM_ENTITY": entity_id, "CRM_ENTITY_TYPE": entity_type})