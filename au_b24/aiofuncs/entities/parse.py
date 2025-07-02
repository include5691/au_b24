import inspect
from typing import Literal, Callable
from ...aioreqs import post
from ..exceptions import StopParsing

def parse_entities(entity_type: Literal["lead", "deal", "contact"], fn: Callable):
    if entity_type not in ["lead", "deal", "contact"]:
        raise ValueError("Entity type incorrect")
    def wrapper(filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC", **kwargs):
        """
        :param filters: filters by fields, allowing '<', '>' and '!' logical symbols, and grouping by []. ID filtering allowing too
        :param select: list of selected fields. Passing '*' will select all fields
        :param order: sorting by id
        """
        async def async_wrapper():
            if not isinstance(filters, dict):
                raise ValueError("Filters and select must be a dict")
            if not select:
                raise ValueError("Select is not provided")
            if not isinstance(select, list):
                raise ValueError("Select must be a list")
            if order not in ("ASC", "DESC"):
                raise ValueError("Order must be 'ASC' or 'DESC'")
            if {">ID", "<ID", ">=ID", "<=ID"} & set(filters):
                raise ValueError("ID filtering can't be used with '<', '>', '>=' and '<='")
            filters_copy = filters.copy()
            if order == "ASC":
                filters_copy.update({">ID": 0})
                id_key = ">ID"
            else:
                filters_copy.update({"<ID": 2**32})
                id_key = "<ID"
            while True:
                entities: list[dict] | None = await post(f"crm.{entity_type}.list", {"filter": filters_copy, "select": select, "order": {"ID": order}, "start": -1})
                if not entities:
                    break
                for entity in entities:
                    if not entity or not isinstance(entity, dict):
                        continue
                    filters_copy[id_key] = entity["ID"]
                    try:
                        if inspect.iscoroutinefunction(fn):
                            await fn(entity, **kwargs)
                        else:
                            fn(entity, **kwargs)
                    except StopParsing:
                        return
        return async_wrapper()
    return wrapper