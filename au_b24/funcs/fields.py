from typing import Literal
from ..reqs import post

def extract_enumerated_field_value(entity_type: Literal["lead", "deal"], field_id: str, key: str | int):
    """Extract enumerated field value by its id and value"""
    if entity_type not in ["lead", "deal"]:
        raise ValueError("entity_type must be 'lead' or 'deal'")
    fields = post(f"crm.{entity_type}.fields", {})
    if not fields:
        return None
    field = fields.get(field_id)
    if not field:
        return None
    if field.get("type") != "enumeration":
        raise ValueError("Field is not enumeration")
    for item in field.get("items"):
        if item.get("ID") == str(key):
            return item.get("VALUE")
    return None