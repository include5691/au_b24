from ...reqs import post

def delete_task(task_id: str | int) -> bool:
    result = post("tasks.task.delete", {"taskId": task_id})
    return bool(result and isinstance(result, dict) and "task" in result and result.get("task"))
