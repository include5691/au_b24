from ...aioreqs import post

async def delete_task(task_id: str | int) -> bool:
    result = await post("tasks.task.delete", {"taskId": task_id})
    return bool(result and isinstance(result, dict) and "task" in result and result.get("task"))
