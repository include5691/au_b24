from .get import get_user

def get_user_name(user_id : int | str | None = None, user : dict | None = None) -> str | None:
    """
    Get user name by user_id or user dict
    """
    if not user_id and not user:
        return None
    if isinstance(user_id, dict) and not user:
        user = user_id
    if user_id and not user:
        user = get_user(user_id)
    if not user:
        return None
    return str(user.get("LAST_NAME")).strip() + " " + str(user.get("NAME")).strip()