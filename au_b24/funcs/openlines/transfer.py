from ...reqs import post, get

def intercept_openline(ol_id: int | str) -> bool | None:
    """
    Intercept openline
    
    Note
    ----
    Needs to transfer dial if get_openlines() returns empty list but get_last_openline_id() returns some id.
    Intersept openline, then transfer it to another user
    """
    result = get("imopenlines.session.intercept", {"CHAT_ID": ol_id})
    return result if result else None

def transfer_openline(ol_id: int | str, user_id: int | str) -> bool | None:
    """
    Transfer openline to providen users
    
    Note
    ----
    May occurs unexplained error with 400 status code - like there is not righ to transfer foreign chat 
    """
    result = post("imopenlines.operator.transfer", {"CHAT_ID": ol_id, "TRANSFER_ID": user_id})
    return result if result else None