from ...reqs import post

def get_session_id(openline_id: int | str) -> int | None:
    """Get session id by given openline_id"""
    result = post("imopenlines.dialog.get", {"CHAT_ID": openline_id})
    if not result or not isinstance(result, dict):
        return None
    entity_data_1 = result.get("entity_data_1")
    if not entity_data_1 or not isinstance(entity_data_1, str):
        return None
    entity_data_parts = entity_data_1.split("|")
    if len(entity_data_parts) != 10:
        return None
    session_id = entity_data_parts[5]
    if not session_id.isdigit():
        return None
    return int(session_id)