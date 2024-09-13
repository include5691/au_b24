from ...reqs import post, get

def intercept_openline(ol_id: int | str) -> bool | None:
    """Intercept openline from another user"""
    result = get("imopenlines.session.intercept", {"CHAT_ID": ol_id})
    return result if result else None

def transfer_openline(ol_id: int | str, user_id: int | str) -> bool | None:
    """
    Transfer openline to providen users
    
    Note
    ----
    May occurs unexplained error with 400 status code (update: only for transfering on yourself)
    """
    result = post("imopenlines.operator.transfer", {"CHAT_ID": ol_id, "TRANSFER_ID": user_id})
    return result if result else None