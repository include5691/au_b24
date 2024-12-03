from ..reqs import get

def get_department(dep_id: str | int) -> dict | None:
    """Get department by its id"""
    dep_list = get("department.get", {"ID": dep_id})
    if not dep_list or not isinstance(dep_list, list):
        return None
    dep = dep_list[0]
    if not dep:
        return None
    return dep