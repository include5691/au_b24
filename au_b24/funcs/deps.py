from ..reqs import get, post

def get_department(dep_id: str | int) -> dict | None:
    """Get department by its id"""
    dep_list = get("department.get", {"ID": dep_id})
    if not dep_list or not isinstance(dep_list, list):
        return None
    dep = dep_list[0]
    if not dep:
        return None
    return dep

def get_all_departaments() -> list[dict] | None:
    """Get all departaments"""
    dep_list = post("department.get", {})
    if not dep_list or not isinstance(dep_list, list):
        return None
    deps = [dep for dep in dep_list if dep and isinstance(dep, dict)]
    return deps if deps else None