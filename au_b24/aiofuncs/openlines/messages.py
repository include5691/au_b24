from ...aioreqs import post

async def get_openline_messages(openline_id: int | str, session_id: int | str) -> list[dict] | None:
    """Get messages by given openline_id and session_id"""
    response = await post("imopenlines.session.history.get", {"CHAT_ID": openline_id, "SESSION_ID": session_id})
    if not response or not isinstance(response, dict):
        return None
    messages_dict = response.get("message")
    if not messages_dict or not isinstance(messages_dict, dict):
        return None
    messages = list(messages_dict.values())
    messages = [message for message in messages if message and isinstance(message, dict)]
    return messages if messages else None