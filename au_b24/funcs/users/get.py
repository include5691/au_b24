from ..._requests import get

def get_user(user_id: int | str) -> dict | None:
    """Get user by user_id"""
    result = get("user.get", {"ID": user_id})
    if result and isinstance(result, list):
        return result[0]
    return None