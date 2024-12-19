from ...reqs import get, post

def get_user(user_id: int | str) -> dict | None:
    """Get user by user_id"""
    result = get("user.get", {"ID": user_id})
    if result and isinstance(result, list):
        return result[0]
    return None

def get_users(filters: dict) -> list[dict] | None:
    """Get users by filters"""
    if {"ID", ">ID", "<ID", ">=ID", "<=ID"} & set(filters):
        raise ValueError("ID filtering is forbidden")
    filters = filters.copy()
    filters[">ID"] = 0
    result = []
    while True:
        users = post("user.get", {"filter": filters, "order": "ASC"})
        if not users or not isinstance(users, list):
            break
        for user in users:
            if not user or not isinstance(user, dict):
                continue
            filters[">ID"] = user["ID"]
            result.append(user)
    return result if result else None