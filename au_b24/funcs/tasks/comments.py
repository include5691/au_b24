from typing import Literal
from ...reqs import post


def get_task_comments(
    task_id: int | str,
    filters: dict,
    order: Literal["asc", "desc"] = "asc",
) -> list[dict]:
    """
    Get comment tasks by filter
    """
    if not isinstance(filters, dict):
        raise ValueError("Filters must be a dict")
    if order not in ("asc", "desc"):
        raise ValueError("Order must be 'asc' or 'desc")
    if {">ID", "<ID", ">=ID", "<=ID"} & set(filters):
        raise ValueError("id filtering can't be used with '<', '>', '>=' and '<='")
    filters_copy = filters.copy()
    if order == "asc":
        filters_copy.update({">ID": 0})
        id_key = ">ID"
    else:
        filters_copy.update({"<ID": 2**32})
        id_key = "<ID"
    result = []
    while True:
        tasks = post(
            "task.commentitem.getlist",
            {
                "TASKID": task_id,
                "ORDER": {"ID": order},
                "FILTER": filters_copy,
                "start": "-1",
            },
        )
        if not tasks or not isinstance(tasks, list):
            return result
        for task in tasks:
            if not task or not isinstance(task, dict):
                continue
            filters_copy[id_key] = task["ID"]
            result.append(task)
