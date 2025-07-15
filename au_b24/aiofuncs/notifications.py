from ..aioreqs import post

async def notify_user(user_id: int | str, message: str) -> int | None:
    """Add notification to user. Returns notification ID"""
    return await post("im.notify.personal.add", {"USER_ID": user_id, "MESSAGE": message})