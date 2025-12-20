from typing import Literal
from ..aioreqs import post


async def add_address(
    entity_type_id: int | str,
    entity_id: int | str,
    type_id: int | str,
    extra_fields: dict | None = None,
) -> bool | None:
    """
    Add address to entity (async)
    Returns creation result
    """
    fields = extra_fields or {}
    fields.update(
        {
            "ENTITY_TYPE_ID": entity_type_id,
            "ENTITY_ID": entity_id,
            "TYPE_ID": type_id,
        }
    )
    return await post(
        "crm.address.add",
        {"fields": fields},
    )


async def get_addresses(
    entity_type_id: int | str,
    entity_id: int | str,
    select: list,
    extra_filters: dict | None = None,
) -> list[dict]:
    """
    Get addresses of entity (async)
    :param entity_type_id: Entity type ID (e.g., 1 for leads, 2 for deals, 3 for contacts, 4 for companies)
    :param entity_id: ID of the entity
    """
    if not isinstance(select, list):
        raise ValueError("Select must be a list")
    if not select:
        raise ValueError("Select is empty")
    filters = {
        "ENTITY_TYPE_ID": entity_type_id,
        "ENTITY_ID": entity_id,
        **(extra_filters or {}),
    }
    addresses = await post(
        "crm.address.list",
        {
            "filter": filters,
            "select": select,
        },
    )
    if not addresses or not isinstance(addresses, list):
        return []
    result: list[dict] = []
    for address in addresses:
        if not address or not isinstance(address, dict):
            continue
        result.append(address)
    return result
