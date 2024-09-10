from ..._requests import post

def transfer_openline(ol_id: int | str, user_id: int | str) -> bool | None:
    """Transfer openline to another user"""
    result = post("imopenlines.operator.transfer", {"CHAT_ID": ol_id, "TRANSFER_ID": user_id})
    return result if result else None