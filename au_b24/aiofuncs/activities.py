from typing import Literal

from .entities import get_entities


async def get_activities(
    filters: dict,
    select: list,
    order: Literal["ASC", "DESC"] = "ASC",
    limit: int | None = None,
) -> list[dict] | None:
    """
    Get activities by filters
    :param filters: filters by fields, allowing '<', '>' and '!' logical symbols, and grouping by []. ID filtering allowing too
    :param select: list of selected fields. Passing '*' will select all fields
    :param order: sorting by id
    """
    return await get_entities(
        entity_type="activity",
        filters=filters,
        select=select,
        order=order,
        limit=limit,
    )
