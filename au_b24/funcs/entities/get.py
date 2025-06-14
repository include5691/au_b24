import logging
from typing import Literal

from ...reqs import post
from ...types_ import EntityType


def get_entities(
    entity_type: EntityType | str,
    filters: dict,
    select: list,
    order: Literal["ASC", "DESC"] = "ASC",
    limit: int | None = None,
) -> list[dict] | None:
    """
    :param filters: filters by fields, allowing '<', '>' and '!' logical symbols, and grouping by []. ID filtering allowing too
    :param select: list of selected fields. Passing '*' will select all fields
    :param order: sorting by id
    """
    if isinstance(entity_type, str):
        try:
            entity_type = EntityType(entity_type)
        except ValueError:
            raise ValueError("Entity type (str) is incorrect")
    if entity_type not in EntityType:
        raise ValueError("Entity type (enum) incorrect")
    if not isinstance(filters, dict):
        raise ValueError("Filters must be a dict")
    if not select:
        raise ValueError("Select is not provided")
    if not isinstance(select, list):
        raise ValueError("Select must be a list")
    if order not in ("ASC", "DESC"):
        raise ValueError("Order must be 'ASC' or 'DESC'")
    if {">ID", "<ID", ">=ID", "<=ID"} & set(filters):
        raise ValueError("ID filtering can't be used with '<', '>', '>=' and '<='")
    if limit and limit <= 0:
        raise ValueError("Limit must be greater than 0")
    filters_copy = filters.copy()
    if order == "ASC":
        filters_copy.update({">ID": 0})
        id_key = ">ID"
    else:
        filters_copy.update({"<ID": 2**32})
        id_key = "<ID"
    result = []
    while True:
        entities: list[dict] | None = post(
            f"crm.{entity_type}.list",
            {
                "filter": filters_copy,
                "select": select,
                "order": {"ID": order},
                "start": -1,
            },
        )
        if not isinstance(entities, (list)):
            logging.error(
                f"Error in request for 'crm.{entity_type}.list' method. Response: {entities}"
            )
            return None
        if not entities:
            break
        for entity in entities:
            if not entity or not isinstance(entity, dict):
                continue
            filters_copy[id_key] = entity["ID"]
            result.append(entity)
            if limit and len(result) >= limit:
                return result
    return result
