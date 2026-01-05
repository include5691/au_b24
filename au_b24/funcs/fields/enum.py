from typing import Literal
from ...reqs import post

def get_enumerated_field_values(entity_type: Literal["lead", "deal", "contact"], field_id: str) -> dict[str, str] | None:
    """Get enumerated field values by field id"""
    if entity_type not in ["lead", "deal", "contact"]:
        raise ValueError("entity_type must be 'lead', 'deal' or 'contact'")
    fields = post(f"crm.{entity_type}.fields", {})
    if not fields:
        return None
    field = fields.get(field_id)
    if not field:
        return None
    if field.get("type") != "enumeration":
        raise ValueError("Field is not enumeration")
    result = {}
    for item in field.get("items", []):
        item_id = item.get("ID")
        item_value = item.get("VALUE")
        if not item_id or not item_value:
            continue
        result[item_id] = item_value
    return result