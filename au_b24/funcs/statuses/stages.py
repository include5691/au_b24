from ...reqs import post

def get_stages(category_id: str | int) -> list[dict] | None:
    """Get stages of deals"""
    stages = post("crm.dealcategory.stage.list", {"id": category_id})
    if not stages or not isinstance(stages, list):
        return None
    return stages