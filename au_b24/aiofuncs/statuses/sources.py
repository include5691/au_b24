from ...aioreqs import post

async def get_sources() -> dict[str, str] | None:
    """Get sources of leads in `id: name` format"""
    sources = await post("crm.status.list", {"filter": {"ENTITY_ID": "SOURCE"}})
    if not sources or not isinstance(sources, list):
        return None
    return {source["STATUS_ID"]: source["NAME"] for source in sources}
