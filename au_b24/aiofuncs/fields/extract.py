from typing import Literal
from ...aioreqs import post

async def extract_enumerated_field_value(entity_type: Literal["lead", "deal"], field_id: str, value: str | int) -> str | None:
    """Extract enumerated field value by its id and value"""
    if entity_type not in ["lead", "deal"]:
        raise ValueError("entity_type must be 'lead' or 'deal'")
    fields = await post(f"crm.{entity_type}.fields", {})
    if not fields:
        return None
    field = fields.get(field_id)
    if not field:
        return None
    if field.get("type") != "enumeration":
        raise ValueError("Field is not enumeration")
    for item in field.get("items"):
        if item.get("ID") == str(value):
            return item.get("VALUE")
    return None

async def extract_enumerated_smart_field_value(entity_id: str | int, field_id: str, value: str | int) -> str | None:
    """Extract enumerated smart process field value by its id and value"""
    response = await post("crm.item.fields", {"entityTypeId": entity_id})
    if not response:
        return None
    fields = response.get("fields")
    if not fields:
        return None
    field = fields.get(field_id)
    if not field:
        return None
    if field.get("type") != "enumeration":
        raise ValueError("Field is not enumeration")
    for item in field.get("items"):
        if item.get("ID") == str(value):
            return item.get("VALUE")
    return None