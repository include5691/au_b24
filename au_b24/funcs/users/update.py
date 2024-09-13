from ...reqs import post

def update_user(user_id: int | str, user_data: dict) -> bool | None:
    """Update user by user_id"""
    result = post("user.update", {"id": user_id, **user_data})
    return result if result else None