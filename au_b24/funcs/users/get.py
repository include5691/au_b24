from ...reqs import get, post

def get_user(user_id: int | str) -> dict | None:
    """Get user by user_id"""
    result = get("user.get", {"ID": user_id})
    if result and isinstance(result, list):
        return result[0]
    return None

def get_users(filters: dict) -> list[dict] | None:
    """Get users by filters"""
    response = post("user.get", {"filter": filters})
    if not response or not isinstance(response, list):
        return None
    users = [user for user in response if user and isinstance(user, dict)]
    return users if users else None