from ...aioreqs import post


async def update_task(task_id: int | str, fields: dict) -> bool:
    """Update task by given task_id and fields"""
    response = await post("tasks.task.update", {"taskId": task_id, "fields": fields})
    return bool(response and isinstance(response, dict) and "task" in response)
