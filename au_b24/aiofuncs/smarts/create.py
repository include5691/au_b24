from ...aioreqs import post

async def create_smart(entity_id: str | int, fields: dict) -> int | None:
    """Create a smart item with the provided entity type id and fields"""
    response = await post("crm.item.add", {"entityTypeId": entity_id, "fields": fields})
    if not response or not isinstance(response, dict):
        return None
    item = response.get("item")
    if not item or not isinstance(item, dict):
        return None
    return item.get("id")
