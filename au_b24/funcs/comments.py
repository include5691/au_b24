from typing import Literal
from ..reqs import post

def add_comment(entity_id: int | str, entity_type: Literal["lead", "deal", "dynamic_*"], text: str) -> int | None:
    """
    Add comment to entity
    Returns comment id
    """
    return post("crm.timeline.comment.add", {"fields": {"ENTITY_ID": entity_id, "ENTITY_TYPE": entity_type, "COMMENT": text}})

def get_comments(entity_id: int | str, entity_type: Literal["lead", "deal", "dynamic_*"], select: list[str]) -> list[dict] | None:
    """
    Get comments of entity
    Due to bug in bitrix api doesn't support filtering by id
    """
    if not isinstance(select, list):
        raise ValueError("Select must be a list")
    if not "ID" in select:
        select.append("ID")
    result = []
    n = 0
    while True:
        comments: list[dict] | None = post(f"crm.timeline.comment.list", {"filter": {"ENTITY_ID": entity_id, "ENTITY_TYPE": entity_type}, "select": select, "order": {"ID": "asc"}, "start": n * 50})
        if not comments:
            break
        for comment in comments:
            if not comment or not isinstance(comment, dict):
                continue
            result.append(comment)
        n += 1
    return result if result else None