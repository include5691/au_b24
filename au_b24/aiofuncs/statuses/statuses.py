from ...aioreqs import post

async def get_statuses() -> dict[str, str] | None:
    """Get statuses of leads bun in `id: name` format"""
    statuses = await post("crm.status.list", {"filter": {"ENTITY_ID": "STATUS"}})
    if not statuses or not isinstance(statuses, list):
        return None
    return {status["STATUS_ID"]: status["NAME"] for status in statuses}