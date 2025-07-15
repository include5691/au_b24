from typing import Literal
from ...aioreqs import post

async def get_stage_history(entity_type: Literal["lead", "deal"], entity_id: str | int, select: list = ["*"], order: Literal["ASC", "DESC"] = "ASC") -> list[dict] | None:
    """
    Get status or stage history
    
    :param select: support ID, TYPE_ID, TYPE_ID, CREATED_TIME, STATUS_SEMANTIC_ID and STATUS_ID fields
    """
    if entity_type == "lead":
        entity_type_id = 1
    elif entity_type == "deal":
        entity_type_id = 2
    else:
        return None
    response = await post("crm.stagehistory.list", {"entityTypeId": entity_type_id, "order": {"ID": order}, "filter": {"OWNER_ID": entity_id}, "select": select, "start": "-1"})
    if not response or not isinstance(response, dict):
        return None
    items =  response.get("items")
    if not items or not isinstance(items, list):
        return None
    result = [item for item in items if item and isinstance(item, dict)]
    return result if result else None