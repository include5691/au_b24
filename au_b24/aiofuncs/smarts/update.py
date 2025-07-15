from ...aioreqs import post

async def update_smart(entity_id: str | int, smart_id: str | int, fields: dict) -> bool:
    """Update smart by given entity type id, smart item id and fields"""
    return bool(await post("crm.item.update", {"entityTypeId": entity_id, "id": smart_id, "fields": fields}))