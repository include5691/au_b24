from ...aioreqs import post

async def get_stages(category_id: str | int) -> dict[str, str] | None:
    """Get stages of deals in `id: name` format"""
    stages = await post("crm.dealcategory.stage.list", {"id": category_id})
    if not stages or not isinstance(stages, list):
        return None
    return {stage["STATUS_ID"]: stage["NAME"] for stage in stages}