from ...aioreqs import get, post

async def get_department(dep_id: str | int) -> dict | None:
    """Get department by its id"""
    dep_list = await get("department.get", {"ID": dep_id})
    if not dep_list or not isinstance(dep_list, list):
        return None
    dep = dep_list[0]
    if not dep:
        return None
    return dep

async def get_all_departaments() -> list[dict] | None:
    """Get all departaments"""
    response = await post("department.get", {})
    if not response or not isinstance(response, list):
        return None
    deps = [dep for dep in response if dep and isinstance(dep, dict)]
    return deps if deps else None

async def get_child_departaments(dep_id: str | int) -> list[dict] | None:
    """Get child departaments by parent departament id"""
    response = await post("department.get", {"PARENT": dep_id})
    if not response or not isinstance(response, list):
        return None
    deps = [dep for dep in response if dep and isinstance(dep, dict)]
    return deps