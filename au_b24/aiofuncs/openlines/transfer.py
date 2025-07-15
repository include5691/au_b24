from ...aioreqs import post, get

async def intercept_openline(ol_id: int | str) -> bool | None:
    """Intercept openline from another user"""
    result = await get("imopenlines.session.intercept", {"CHAT_ID": ol_id})
    return result if result else None

async def transfer_openline(ol_id: int | str, user_id: int | str) -> bool | None:
    """
    Transfer openline to providen users
    
    Note
    ----
    May occurs unexplained error with 400 status code (update: only for transfering on yourself)
    """
    result = await post("imopenlines.operator.transfer", {"CHAT_ID": ol_id, "TRANSFER_ID": user_id})
    return result if result else None