from typing import Literal
from ...reqs import post

def get_field(entity_type: Literal["lead", "deal", "contact"], field_id: str) -> dict[str, str] | None:
    """Get field by field id"""
    if entity_type not in ["lead", "deal", "contact"]:
        raise ValueError("entity_type must be 'lead', 'deal' or 'contact'")
    fields = post(f"crm.{entity_type}.fields", {})
    if not fields:
        return None
    field = fields.get(field_id)
    if not field:
        return None
    return field