from .get import get_department


def get_dep_name(
    dep_id: str | int | None = None, dep: dict | None = None
) -> str | None:
    """
    Get department name by dep_id or dep dict
    """
    if dep_id and isinstance(dep_id, dict):
        dep = dep_id
    dep = dep or get_department(dep_id)
    if not dep or not isinstance(dep, dict):
        return None
    return str(dep.get("NAME")).strip() if "NAME" in dep else None
