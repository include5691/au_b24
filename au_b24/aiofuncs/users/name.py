from .get import get_user

async def get_user_name(user_id: int | str | None = None, user: dict | None = None) -> str | None:
    """
    Get user name by user_id or user dict
    """
    if user_id and isinstance(user_id, dict):
        user = user_id
    user = user or await get_user(user_id)
    if not user or not isinstance(user, dict):
        return None
    return str(user.get("LAST_NAME")).strip() + " " + str(user.get("NAME")).strip()