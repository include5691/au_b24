from typing import Literal, Callable
from ...reqs import post
from ..exceptions import StopParsing

def parse_entities(entity_type: Literal["lead", "deal", "contact"], fn: Callable):
    if entity_type not in ["lead", "deal", "contact"]:
        raise ValueError("Entity type incorrect")
    def wrapper(filters: dict, select: list, order: Literal["ASC", "DESC"] = "ASC", allow_id_filter: bool = False, **kwargs):
        """
        :param filters: filters by fields, allowing '<', '>' and '!' logical symbols, and grouping by []. ID filtering allowing too
        :param select: list of selected fields. Passing '*' will select all fields
        :param order: sorting by id
        """
        if not isinstance(filters, dict):
            raise ValueError("Filters and select must be a dict")
        if not select:
            raise ValueError("Select is not provided")
        if not isinstance(select, list):
            raise ValueError("Select must be a list")
        if order not in ("ASC", "DESC"):
            raise ValueError("Order must be 'ASC' or 'DESC'")
        id_keys = list({">ID", "<ID", ">=ID", "<=ID"} & set(filters))
        if id_keys:
            if not allow_id_filter:
                raise ValueError("ID filtering can't be used with '<', '>', '>=' and '<='")
            allow_id_filter = True
            for key in id_keys[1:]:
                del filters[key]
            id_key = id_keys.pop()
            if "<" in id_key:
                order = "DESC"
            elif ">" in id_key:
                order = "ASC"
        else:
            if allow_id_filter:
                allow_id_filter = False
        filters_copy = filters.copy()
        if not allow_id_filter:
            if order == "ASC":
                filters_copy.update({">ID": 0})
                id_key = ">ID"
            else:
                filters_copy.update({"<ID": 2**32})
                id_key = "<ID"
        counter = 0
        while True:
            entities: list[dict] | None = post(f"crm.{entity_type}.list", {"filter": filters_copy, "select": select, "order": {"ID": order}, "start": -1})
            if not entities:
                break
            for entity in entities:
                if not entity or not isinstance(entity, dict):
                    continue
                filters_copy[id_key] = entity["ID"]
                try:
                    counter += 1
                    fn(entity, counter=counter, **kwargs)
                except StopParsing:
                    return
    return wrapper