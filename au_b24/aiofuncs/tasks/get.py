from typing import Literal
from ...aioreqs import post


async def get_task(task_id: int | str, select: list | None = None) -> dict | None:
    """Get task by given task_id"""
    data = {"taskId": task_id}
    if select:
        data["select"] = select
    response = await post("tasks.task.get", data)
    if not response or not isinstance(response, dict) or "task" not in response:
        return None
    return response["task"]


async def get_tasks(
    filters: dict,
    select: list,
    order: Literal["asc", "desc"] = "asc",
    limit: int | None = None,
) -> list[dict]:
    """
    Get tasks by filter
    To filter by CRM entity use 'UF_CRM_TASK' field, 'D_<deal_id>' for deals, 'L_<lead_id>' for leads
    NOTE: 'id' field name is lower
    """
    if not isinstance(filters, dict):
        raise ValueError("Filters must be a dict")
    if not select:
        raise ValueError("Select is not provided")
    if not isinstance(select, list):
        raise ValueError("Select must be a list")
    if order not in ("asc", "desc"):
        raise ValueError("Order must be 'asc' or 'desc")
    if {">ID", "<ID", ">=ID", "<=ID"} & set(filters):
        raise ValueError("id filtering can't be used with '<', '>', '>=' and '<='")
    if limit and limit <= 0:
        raise ValueError("Limit must be greater than 0")
    filters_copy = filters.copy()
    if order == "asc":
        filters_copy.update({">ID": 0})
        id_key = ">ID"
    else:
        filters_copy.update({"<ID": 2**32})
        id_key = "<ID"
    result = []
    while True:
        response = await post(
            "tasks.task.list",
            {
                "filter": filters_copy,
                "select": select,
                "order": {"ID": order},
                "start": "-1",
            },
        )
        if not response or not "tasks" in response:
            break
        tasks = response["tasks"]
        if not tasks or not isinstance(tasks, list):
            return result
        for task in tasks:
            if not task or not isinstance(task, dict):
                continue
            filters_copy[id_key] = task["id"]
            result.append(task)
            if limit and len(result) >= limit:
                return result
