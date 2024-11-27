from typing import Literal
from ..reqs import post

def add_comment(entity_id: int | str, entity_type: Literal["lead", "deal", "dynamic_*"], text: str) -> int | None:
    """
    Add comment to entity
    Returns comment id
    """
    return post("crm.timeline.comment.add", {"fields": {"ENTITY_ID": entity_id, "ENTITY_TYPE": entity_type, "COMMENT": text}})