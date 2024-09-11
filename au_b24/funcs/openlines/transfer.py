from ..._requests import post

def transfer_openline(ol_id: int | str, user_id: int | str) -> bool | None:
    """
    Transfer openline to providen users
    
    Note
    ----
    May occurs unexplained error with 400 status code - like there is not righ to transfer foreign chat 
    """
    result = post("imopenlines.operator.transfer", {"CHAT_ID": ol_id, "TRANSFER_ID": user_id})
    return result if result else None