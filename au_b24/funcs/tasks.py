from typing import Literal
from ..reqs import post

def get_tasks(filters: dict, select: list, order: Literal['asc', 'desc'] = 'asc') -> list[dict]:
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
    if order not in ('asc', 'desc'):
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
        response = post("tasks.task.list", {"filter": filters_copy, "select": select, 'order': {"ID": order}, "start": "-1"})
        if not response or not "tasks" in response:
            break
        tasks = response["tasks"]
        if not tasks or not isinstance(tasks, list):
            break
        for task in tasks:
            if not task or not isinstance(task, dict):
                continue
            filters_copy[id_key] = task["id"]
            result.append(task)
    return result

def delete_task(task_id: str | int) -> bool:
    result = post("tasks.task.delete", {"taskId": task_id})
    return bool(result and isinstance(result, dict) and "task" in result and result.get("task"))

def add_task(title: str, created_by: str | int, responsible_id: str | int, extra_fields: dict | None = None) -> int | None:
    "Create tasks with mandatory and arbitrary (extra) fields"
    result = post("tasks.task.add", {"fields": {"TITLE": title, "CREATED_BY": created_by, "RESPONSIBLE_ID": responsible_id} | (extra_fields or {})})
    if not result or not isinstance(result, dict):
        return
    task = result.get("task")
    if not task or not isinstance(task, dict):
        return
    task_id = task.get("id")
    if not task_id or not isinstance(task_id, str) or not task_id.isdecimal():
        return
    return int(task_id)