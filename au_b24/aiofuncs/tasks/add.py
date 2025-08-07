from ...aioreqs import post

async def add_task(title: str | None = None, created_by: str | int | None = None, responsible_id: str | int | None = None, extra_fields: dict | None = None, **kwargs) -> int | None:
    "Create tasks with mandatory and arbitrary (extra) fields"
    extra_fields = extra_fields or {}
    if kwargs:
        if "TITLE" in kwargs:
            title = kwargs["TITLE"]
        if "CREATED_BY" in kwargs:
            created_by = kwargs["CREATED_BY"]
        if "RESPONSIBLE_ID" in kwargs:
            responsible_id = kwargs["RESPONSIBLE_ID"]
        extra_fields.update(kwargs)
    extra_fields_formatted = {}
    keys_to_skip = {"ID", "CREATED_BY", "RESPONSIBLE_ID"}
    for k, v in extra_fields.items():
        if isinstance(k, str):
            key = k.upper()
            if key in keys_to_skip:
                continue
            extra_fields_formatted[key] = v
    result = await post("tasks.task.add", {"fields": {"TITLE": title, "CREATED_BY": created_by, "RESPONSIBLE_ID": responsible_id} | extra_fields_formatted})
    if not result or not isinstance(result, dict):
        return
    task = result.get("task")
    if not task or not isinstance(task, dict):
        return
    task_id = task.get("id")
    if not task_id or not isinstance(task_id, str) or not task_id.isdecimal():
        return
    return int(task_id)
